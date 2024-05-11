# Ubicuo

## esp32.ino
### es el codigo que tiene la esp32, se tiene que adaptar el sensor
### el codigo actual se conecta a una red wifi, se tiene que cambiar el *ssid y *password para que coincida con la red a la que se quiere conectar, tiene que ser la misma red a la que este conectada la computadora
### tambien sse tiene que cambiar el *server con la ip de la computadora en donde se corre el server
### el port debe mantenerse igual 
### el codigo manda un mensaje a un servidor, este mensaje funciona como una contraseña que se verifica en el servidor, tambien manda la ip del esp32 (candy nos dijo que la ubicacion la saquemos desde la ip del esp32)

## serv2.py
### el HOST y PORT se deben mantener igual
### fastapi_url cambiara con el url de la aplicacion que despliguen 
### el servidor recibe el mensaje de la esp32 y la ip, al confirmar que el mensaje coincide activa el reconocimiento de voz, guarda lo que dices y lo envia a la aplicacion en la nube junto a la ip

## serv3.py
### codigo de respaldo del servidor, hace todo lo anterior pero sin la parte en la que envia el mensaje a la aplicacion en la nube

## env.py
### sirve para enviar un mensaje a la aplicacion en la nube (uniendo este codigo con el de serv3 se obtiene el serv2)
### fastapi_url cambiara con el url de la aplicacion que despliguen

## nube
### en la carpeta nube estan 3 archivos necesarios para desplegar la aplciacion en la nube

## nube/main.py
### en este archivo esta el codigo de la aplicacion en la nube, esta a la espera de mensajes 

## Deploy your FastAPI app in serverless Google App Engine (1).pdf
### este es el pdf la practica que pidio candy para desplegar una aplicacion en la nube, seguir a partir del paso 4

## verificar si llegan los mensajes
### en el google cloud accedan al explorador de registros, aqui podran ver cuando lleguen los mensajes 
![image](https://github.com/Ulises-castellanos/Ubicuo/assets/78512508/117a702a-bdd8-4650-bbd8-d262e7b3ca18)


