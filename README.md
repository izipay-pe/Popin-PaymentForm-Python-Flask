<p align="center">
  <img src="https://github.com/izipay-pe/Imagenes/blob/main/logos_izipay/logo-izipay-banner-1140x100.png?raw=true" alt="Formulario" width=100%/>
</p>

# Popin-PaymentForm-Python-Flask

## Índice

➡️ [1. Introducción](https://github.com/izipay-pe/Popin-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#%EF%B8%8F-1-introducci%C3%B3n)  
🔑 [2. Requisitos previos](https://github.com/izipay-pe/Popin-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#-2-requisitos-previos)  
🚀 [3. Ejecutar ejemplo](https://github.com/izipay-pe/Popin-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#-3-ejecutar-ejemplo)  
🔗 [4. Pasos de integración](https://github.com/izipay-pe/Popin-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#4-pasos-de-integraci%C3%B3n)  
💻 [4.1. Desplegar pasarela](https://github.com/izipay-pe/Popin-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#41-desplegar-pasarela)  
💳 [4.2. Analizar resultado de pago](https://github.com/izipay-pe/Popin-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#42-analizar-resultado-del-pago)  
📡 [4.3. Pase a producción](https://github.com/izipay-pe/Popin-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#43pase-a-producci%C3%B3n)  
🎨 [5. Personalización](https://github.com/izipay-pe/Popin-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#-5-personalizaci%C3%B3n)  
📚 [6. Consideraciones](https://github.com/izipay-pe/Popin-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#-6-consideraciones)

## ➡️ 1. Introducción

En este manual podrás encontrar una guía paso a paso para configurar un proyecto de **[PYTHON]** con la pasarela de pagos de IZIPAY. Te proporcionaremos instrucciones detalladas y credenciales de prueba para la instalación y configuración del proyecto, permitiéndote trabajar y experimentar de manera segura en tu propio entorno local.
Este manual está diseñado para ayudarte a comprender el flujo de la integración de la pasarela para ayudarte a aprovechar al máximo tu proyecto y facilitar tu experiencia de desarrollo.

> [!IMPORTANT]
> En la última actualización se agregaron los campos: **nombre del tarjetahabiente** y **correo electrónico** (Este último campo se visualizará solo si el dato no se envía en la creación del formtoken).

<p align="center">
  <img src="https://github.com/izipay-pe/Imagenes/blob/main/formulario_popin/Imagen-Formulario-Popin.png?raw=true" alt="Formulario" width="350"/>
</p>

## 🔑 2. Requisitos Previos

- Comprender el flujo de comunicación de la pasarela. [Información Aquí](https://secure.micuentaweb.pe/doc/es-PE/rest/V4.0/javascript/guide/start.html)
- Extraer credenciales del Back Office Vendedor. [Guía Aquí](https://github.com/izipay-pe/obtener-credenciales-de-conexion)
- Para este proyecto utilizamos Python 3.12
- Para este proyecto utilizamos la herramienta Visual Studio Code.

> [!NOTE]
> Tener en cuenta que, para que el desarrollo de tu proyecto, eres libre de emplear tus herramientas preferidas.

## 🚀 3. Ejecutar ejemplo

### Instalar Plugin "Python"
Python, extensión para Visual Studio Code que ofrece soporte completo para el lenguaje Python (para todas las versiones del lenguaje >= 3.7). Para instalarlo:
1. Ingresar a la sección "Extensiones" de Visual Studio Code
2. Buscar "Python"
3. Instalar extensión

<p align="center">
  <img src="https://i.postimg.cc/XYZKRcNJ/Plugin.png" alt="Plugin" width="850"/>
</p>

### Clonar el proyecto
```sh
git clone https://github.com/izipay-pe/Popin-PaymentForm-Python-Flask
```

### Datos de conexión 

Reemplace **[CHANGE_ME]** con sus credenciales de `API REST` extraídas desde el Back Office Vendedor, revisar [Requisitos previos](https://github.com/izipay-pe/Popin-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#-2-requisitos-previos).

- Editar el archivo `key.py` en la ruta raíz:
```python
credentials = {
    "USERNAME": "CHANGE_ME_USER_ID",
    "PASSWORD": "CHANGE_ME_PASSWORD",
    "PUBLIC_KEY": "CHANGE_ME_PUBLIC_KEY",
    "HMACSHA256": "CHANGE_ME_HMAC_SHA_256"
}
```

### Preparar el entorno:
Antes de ejecutar el proyecto, se creará el virtual environment (venv):
1. Presionar `ctrl` + `shift` + `p` para abrir la paleta de comandos y buscar `Python: Select Interpreter`
<p align="center">
  <img src="https://i.postimg.cc/yYpXprHt/Select-Interpreter.png" alt="PanelComandos" width="600"/>
</p>
2. Seleccionar `Create Virtual Environment`
<p align="center">
  <img src="https://i.postimg.cc/43fcJ6sV/Create-Env.png" alt="CreateVenv" width="600"/>
</p>
3. Seleccionar el tipo de venv
<p align="center">
  <img src="https://i.postimg.cc/PJ2zjS8L/Venv.png" alt="SelectVenv" width="600"/>
</p>
4. Seleccionar la versión de Python
<p align="center">
  <img src="https://i.postimg.cc/1RHKw3Y9/Select-Python.png" alt="SelectPython" width="600"/>
</p>
5. Seleccionar archivo de dependencias `requirements.txt`
<p align="center">
  <img src="https://i.postimg.cc/pr2Y4wyb/Requirements.png" alt="SelectRequirements" width="600"/>
</p>

### Ejecutar proyecto
1. Para ejecutar el proyecto a través de Visual Studio, ingresar a la sección "Ejecutar" y seleccionar `Run and Debug`
<p align="center">
  <img src="https://i.postimg.cc/8sQdxm4D/Ejecutar.png" alt="SelectInterpreter" width="400"/>
</p>
2. Seleccionar el debugger: `Python Debugger`
<p align="center">
  <img src="https://i.postimg.cc/yxSXfbFv/Debugger.png" alt="SelectRequirements" width="600"/>
</p>
3. Seleccionar la configuración del debugger `Flask`
<p align="center">
  <img src="https://i.postimg.cc/wvrQQps1/Debug-conf.png" alt="SelectRequirements" width="600"/>
</p>
4. El proyecto se ha ejecutado y es accesible a través de:

 ```sh
  http://127.0.0.1:5000
 ```

## 🔗4. Pasos de integración

<p align="center">
  <img src="https://i.postimg.cc/pT6SRjxZ/3-pasos.png" alt="Formulario" />
</p>

## 💻4.1. Desplegar pasarela
### Autentificación
Extraer las claves de `usuario` y `contraseña` del Backoffice Vendedor, concatenar `usuario:contraseña` y agregarlo en la solicitud del encabezado `Authorization`. Podrás encontrarlo en el archivo `app.py`.

```python
@app.post('/checkout')
def formulario():
    ...
    ...
    auth = 'Basic ' + base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('utf-8')
```

ℹ️ Para más información: [Autentificación](https://secure.micuentaweb.pe/doc/es-PE/rest/V4.0/javascript/guide/embedded/keys.html)
### Crear formtoken
Para configurar la pasarela se necesita generar un formtoken. Se realizará una solicitud API REST a la api de creación de pagos:  `https://api.micuentaweb.pe/api-payment/V4/Charge/CreatePayment` con los datos de la compra para generar el formtoken. Podrás encontrarlo en el archivo `app.py`.

```python
@app.post('/checkout')
def formulario():
    ...
    ...
    
    # Definir la URL del endpoint
    url = 'https://api.micuentaweb.pe/api-payment/V4/Charge/CreatePayment'
    # Definir la autenticación para la API
    auth = 'Basic ' + base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('utf-8')
   
    # Definir el body de la solicitud
    data = {
        "amount": int(Decimal(request.form["amount"]) * 100),
        ...
        ...
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
```
ℹ️ Para más información: [Formtoken](https://secure.micuentaweb.pe/doc/es-PE/rest/V4.0/javascript/guide/embedded/formToken.html)
### Visualizar formulario
Para desplegar la pasarela, configura la llave `public key` en el encabezado (Header) del archivo `checkout.html`. Esta llave debe ser extraída desde el Back Office del Vendedor.

Header: 
Se coloca el script de la libreria necesaria para importar las funciones y clases principales de la pasarela. Podrás encontrarlo en el archivo `templates/checkout.html`.
```html
<script type="text/javascript"
              src="https://static.micuentaweb.pe/static/js/krypton-client/V4.0/stable/kr-payment-form.min.js"
              kr-public-key="{{data.public_key}}"
              kr-post-url-success="result">
</script>

<link rel="stylesheet" href="https://static.micuentaweb.pe/static/js/krypton-client/V4.0/ext/classic.css">
<script type="text/javascript" src="https://static.micuentaweb.pe/static/js/krypton-client/V4.0/ext/classic.js">
</script>
```
Además, se inserta en el body una etiqueta div con la clase `kr-embedded` que deberá tener el atributo `kr-form-token` e incrustarle el `formtoken` generado en la etapa anterior.

Body:
```html
<div id="micuentawebstd_rest_wrapper">
	<!-- HTML para incrustar la pasarela de pagos-->
	<div class="kr-embedded" kr-popin kr-form-token="{{data.formToken}}"></div>	
</div>
```
ℹ️ Para más información: [Visualizar formulario](https://secure.micuentaweb.pe/doc/es-PE/rest/V4.0/javascript/guide/embedded/formToken.html)

## 💳4.2. Analizar resultado del pago

### Validación de firma
Se realizará la validación de la firma con los datos del parámetro `kr-answer` utilizando una clave de encriptacón definida por el parámetro `kr-hash-key`. Podrás encontrarlo en el archivo `app.py`.

```python
@app.post('/result')
def paidResult():
    # Asignando los valores de la respuesta de Izipay en las variables
    krHash = request.form.get('kr-hash')
    ...
    ...
    
    # Calculamos un Hash usando el valor del 'kr-answer' y el valor del 'kr-hash-key'
    hash_object = hmac.new(credentials['HMACSHA256'].encode('utf-8'), answer.encode('utf-8'), hashlib.sha256)
    answerHash = hash_object.hexdigest()
    
    ...
    ...
```

Se valida que la firma recibida es correcta. Podrás encontrarlo en el archivo `app.py`.

```python
@app.post('/result')
def paidResult():

    ...
    ...
    
    # Verifica la integridad del Hash recibido y el generado
    if krHash == answerHash:
        ...
        ...
```

En caso que la validación sea exitosa, se puede mostrar los datos de `kr-answer` a través de un JSON y mostrar los datos del pago realizado. Podrás encontrarlo en el archivo `app.py`.

```python
@app.post('/result')
def paidResult():
    
    ...
    ...

    answer = request.form.get('kr-answer')
    # Convertir el kr-answer en Json
    answer_json = json.loads(answer)
    # Formatear el Json a Pretty Json
    pjson = json.dumps(answer_json, indent=2, ensure_ascii=False)
    
    # Verifica la integridad del Hash recibido y el generado
    if krHash == answerHash:
        # Renderiza el template enviando los valores de la transacción
        return render_template('result.html', krHash=krHash, krHashAlgorithm=krHashAlgorithm, krAnswerType=krAnswerType, data=answer_json, krHashKey=krHashKey, pjson=pjson)
    else:
        return render_template('result.html', data={'response': 'Error en el pago'})
```
ℹ️ Para más información: [Analizar resultado del pago](https://secure.micuentaweb.pe/doc/es-PE/rest/V4.0/kb/payment_done.html)

### IPN
La IPN es una notificación de servidor a servidor (servidor de Izipay hacia el servidor del comercio) que facilita información en tiempo real y de manera automática cuando se produce un evento, por ejemplo, al registrar una transacción.

Se realizará la validación de la firma con los datos del parámetro `kr-answer` utilizando una clave de encriptacón definida por el parámetro `kr-hash-key` y se devuelve al servidor de izipay un mensaje confirmando el estado del pago. Podrás encontrarlo en el archivo `app.py`.

```python
@app.post('/ipn')
def ipn():
    # Asignando los valores de la respuesta IPN en las variables
    krHash = request.form.get('kr-hash')
    answer = request.form.get('kr-answer')
    
    # Calculamos un Hash usando el valor del 'kr-answer' y el valor del 'kr-hash-key'
    hash_object = hmac.new(credentials['PASSWORD'].encode('utf-8'), answer.encode('utf-8'), hashlib.sha256)
    answerHash = hash_object.hexdigest()

    # Convertir el kr-answer en Json
    answer_json = json.loads(answer)
    
    # Verifica la integridad del Hash recibido y el generado
    if krHash == answerHash:
        # Imprime en la terminal el Order Status
        print("OK! Order Status is " + answer_json['orderStatus'])
        # Retorna una respuesta HTTP 200
        return 'Correcto', 200
```

La IPN debe ir configurada en el Backoffice Vendedor, en `Configuración -> Reglas de notificación -> URL de notificación al final del pago`

<p align="center">
  <img src="https://i.postimg.cc/zfx5JbQP/ipn.png" alt="Formulario" width=80%/>
</p>

ℹ️ Para más información: [Analizar IPN](https://secure.micuentaweb.pe/doc/es-PE/rest/V4.0/api/kb/ipn_usage.html)

### Transacción de prueba

Antes de poner en marcha su pasarela de pago en un entorno de producción, es esencial realizar pruebas para garantizar su correcto funcionamiento.

Puede intentar realizar una transacción utilizando una tarjeta de prueba con la barra de herramientas de depuración (en la parte inferior de la página).

<p align="center">
  <img src="https://i.postimg.cc/3xXChGp2/tarjetas-prueba.png" alt="Formulario"/>
</p>

- También puede encontrar tarjetas de prueba en el siguiente enlace. [Tarjetas de prueba](https://secure.micuentaweb.pe/doc/es-PE/rest/V4.0/api/kb/test_cards.html)

## 📡4.3.Pase a producción

Reemplace **[CHANGE_ME]** con sus credenciales de PRODUCCIÓN de `API REST` extraídas desde el Back Office Vendedor, revisar [Requisitos Previos](https://github.com/izipay-pe/Popin-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#-2-requisitos-previos).

- Editar el archivo `key.py` en la ruta raíz:
```python
credentials = {
    "USERNAME": "CHANGE_ME_USER_ID",
    "PASSWORD": "CHANGE_ME_PASSWORD",
    "PUBLIC_KEY": "CHANGE_ME_PUBLIC_KEY",
    "HMACSHA256": "CHANGE_ME_HMAC_SHA_256"
}
```

## 🎨 5. Personalización

Si deseas aplicar cambios específicos en la apariencia de la pasarela de pago, puedes lograrlo mediante la modificación de código CSS. En este enlace [Código CSS - Popin](https://github.com/izipay-pe/Personalizacion/blob/main/Formulario%20Popin/Style-Personalization-PopIn.css) podrá encontrar nuestro script para un formulario incrustado.

<p align="center">
  <img src="https://github.com/izipay-pe/Imagenes/blob/main/formulario_popin/Imagen-Formulario-Custom-Popin.png" alt="Formulario"/>
</p>


## 📚 6. Consideraciones

Para obtener más información, echa un vistazo a:

- [Formulario incrustado: prueba rápida](https://secure.micuentaweb.pe/doc/es-PE/rest/V4.0/javascript/quick_start_js.html)
- [Primeros pasos: pago simple](https://secure.micuentaweb.pe/doc/es-PE/rest/V4.0/javascript/guide/start.html)
- [Servicios web - referencia de la API REST](https://secure.micuentaweb.pe/doc/es-PE/rest/V4.0/api/reference.html)

