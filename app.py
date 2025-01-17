from flask import Flask, request, render_template, redirect, url_for, json
from datetime import datetime
import base64
import requests
import json
import hmac
import hashlib
from key import credentials
from decimal import Decimal

app = Flask(__name__)

# Manejo de solicitudes GET para la ruta raíz
@app.get('/')
def index():
    # Generar un número de orden
    order = datetime.now().strftime("Order-%Y%m%d%H%M%S")
    args = request.args
    # Renderizar el template y enviar el orderID
    return render_template('index.html', data={"order": order})

# Manejo de solicitudes POST para la ruta checkout
@app.post('/checkout')
def formulario():
    # Obtener el usuario y las claves API
    username = credentials["USERNAME"]
    password = credentials["PASSWORD"]
    publickey = credentials['PUBLIC_KEY']
    
    # Definir la URL del endpoint
    url = 'https://api.micuentaweb.pe/api-payment/V4/Charge/CreatePayment'
    # Definir la autenticación para la API
    auth = 'Basic ' + base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('utf-8')
   
    # Definir el body de la solicitud
    data = {
        "amount": int(Decimal(request.form["amount"]) * 100),
        "currency": request.form["currency"],
        "customer": {
            "email": request.form["email"],
            "billingDetails": {
                "firstName": request.form["firstName"],
                "lastName": request.form["lastName"],
                "identityType": request.form["identityType"],
                "identityCode": request.form["identityCode"],
                "phoneNumber": request.form["phoneNumber"],
                "address": request.form["address"],
                "country": request.form["country"],
                "state": request.form["state"],
                "city": request.form["city"],
                "zipCode": request.form["zipCode"]
            }
        },
        "orderId": request.form["orderId"]
    }
    
    # Definir los encabezados de la solicitud
    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth,
    }

    # Crear la conexión a la API para la creación del FormToken
    response = requests.post(url, json=data, headers=headers)
    # Obtener la respuesta de la solicitud
    response_data = response.json()

    # Ingresa a la condicional si la repuesta es válida
    if response_data['status'] == 'SUCCESS':
        # Extraer el FormToken
        formToken = response_data['answer']['formToken']
        # Renderizar el template con el formToken y el publicKey
        return render_template("checkout.html", data={"formToken": formToken, "public_key": publickey})
    else:
        serialized_data = json.dumps(response_data, indent=4)
        return render_template('error.html', data={'serialized_data': serialized_data})


# Manejo de solicitudes POST para la ruta result
@app.post('/result')
def paidResult():
    if not request.form: raise Exception("no post data received!")
    
    if not checkHash(request.form, credentials["HMACSHA256"]) : raise Exception("Invalid signature")

    # Asignando los valores de la respuesta de Izipay en las variables
    krHash = request.form.get('kr-hash')
    krHashAlgorithm = request.form.get('kr-hash-algorithm')
    krAnswerType = request.form.get('kr-answer-type')
    answer = request.form.get('kr-answer')
    krHashKey = request.form.get('kr-hash-key')
    
    # Convertir el kr-answer en Json
    answer_json = json.loads(answer)
    # Formatear el Json a Pretty Json
    pjson = json.dumps(answer_json, indent=2, ensure_ascii=False)
    
    # Renderiza el template enviando los valores de la transacción
    return render_template('result.html', krHash=krHash, krHashAlgorithm=krHashAlgorithm, krAnswerType=krAnswerType, data=answer_json, krHashKey=krHashKey, pjson=pjson)


# Manejo de solicitudes POST para la ruta ipn
@app.post('/ipn')
def ipn():
    if not request.form: raise Exception("no post data received!")
    
    if not checkHash(request.form, credentials["PASSWORD"]) : raise Exception("Invalid signature")

    # Asignando los valores de la respuesta IPN en las variables
    answer = request.form.get('kr-answer')

    # Convertir el kr-answer en Json
    answer_json = json.loads(answer)

    transaction = answer_json['transactions'][0]
    orderStatus = answer_json['orderStatus']
    orderId = answer_json['orderDetails']['orderId']
    transactionUuid = transaction['uuid']
    
    # Retorna una respuesta HTTP 200
    return 'OK! OrderStatus is ' + orderStatus, 200


def checkHash(reqPost, key):
    answerHash = hmac.new(key.encode('utf-8'), reqPost.get("kr-answer").encode('utf-8'), hashlib.sha256).hexdigest()
    hash = reqPost.get('kr-hash')
    return hash == answerHash

if __name__ == '__main__':
    app.run(debug=True)
