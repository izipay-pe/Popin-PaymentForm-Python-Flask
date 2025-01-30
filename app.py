from flask import Flask, request, render_template, redirect, url_for, json
from datetime import datetime
import base64
import requests
import json
import hmac
import hashlib
from key import keys
from decimal import Decimal

app = Flask(__name__)

@app.get('/')
def index():
    # Generar un número de orden
    order = datetime.now().strftime("Order-%Y%m%d%H%M%S")
    return render_template('index.html', data={"order": order})

@app.post('/checkout')
def formulario():
    #URL de Web Service REST
    url = 'https://api.micuentaweb.pe/api-payment/V4/Charge/CreatePayment'

    #Encabezado Basic con concatenación de "usuario:contraseña" en base64
    auth = 'Basic ' + base64.b64encode(f"{keys["USERNAME"]}:{keys["PASSWORD"]}".encode('utf-8')).decode('utf-8')
   
    headers = {
    'Content-Type': 'application/json',
    'Authorization': auth,
    }

    data = {
        "amount": int(Decimal(request.form["amount"]) * 100),
        "currency": request.form["currency"],
        "orderId": request.form["orderId"],
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
        }
    }

    # Crear la conexión a la API para la creación del FormToken
    response = requests.post(url, json=data, headers=headers)
    response_data = response.json()

    # Ingresa a la condicional si la repuesta es válida
    if response_data['status'] == 'SUCCESS':
        # Extraer el FormToken
        formToken = response_data['answer']['formToken']
        return render_template("checkout.html", data={"formToken": formToken, "public_key": keys['PUBLIC_KEY']})
    else:
        serialized_data = json.dumps(response_data, indent=4)
        return render_template('error.html', data={'serialized_data': serialized_data})

@app.post('/result')
def paidResult():
    if not request.form: 
        raise Exception("No post data received!")
    
    #Validación de firma
    if not checkHash(request.form, keys["HMACSHA256"]): 
        raise Exception("Invalid signature")
    
    # Asignando los valores de la respuesta IPN en las variables
    answer_json = json.loads(request.form.get('kr-answer'))
    krAnswerData = json.dumps(answer_json, indent=2)
    postData = json.dumps(request.form, indent=4)
    
    return render_template('result.html', data=answer_json, postData=postData, krAnswerData=krAnswerData)

@app.post('/ipn')
def ipn():
    if not request.form: 
        raise Exception("No post data received!")
    
    #Validación de firma en IPN
    if not checkHash(request.form, keys["PASSWORD"]): 
        raise Exception("Invalid signature")

    answer = json.loads(request.form.get('kr-answer')) 
    transaction = answer['transactions'][0]

    #Verificar orderStatus: PAID / UNPAID
    orderStatus = answer['orderStatus']
    orderId = answer['orderDetails']['orderId']
    transactionUuid = transaction['uuid']
    
    return 'OK! OrderStatus is ' + orderStatus, 200


def checkHash(response, key):
    answer = response['kr-answer'].encode('utf-8')
    calculateHash = hmac.new(key.encode('utf-8'), answer, hashlib.sha256).hexdigest()
    return calculateHash == response['kr-hash']

if __name__ == '__main__':
    app.run(debug=True)
