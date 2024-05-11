import requests

# URL de tu aplicación FastAPI desplegada en Google Cloud Platform
fastapi_url = 'https://fastapi-deploy-example-421202.uc.r.appspot.com/receive_message'

# Mensaje que deseas enviar
message = 'hola como estas?'

# Enviar el mensaje mediante una solicitud POST con el mensaje como un parámetro de consulta en la URL
response = requests.post(fastapi_url + f'?message={message}')

# Verificar si la solicitud se completó con éxito
if response.status_code == 200:
    print("El mensaje se envió correctamente.")
else:
    print("Hubo un problema al enviar el mensaje:")
    print(response.text)  # Imprimir cualquier mensaje de error devuelto por el servidor
