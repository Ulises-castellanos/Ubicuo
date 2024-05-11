import socket
import speech_recognition as sr

# Configura el servidor
HOST = '0.0.0.0'  # Escucha en todas las interfaces de red
PORT = 12345       # Puerto para escuchar las conexiones

# Mensaje esperado del ESP32
expected_message = "Mensaje desde ESP32"

# Crear un socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Vincular el socket a la dirección y el puerto
    s.bind((HOST, PORT))
    # Escuchar conexiones entrantes
    s.listen()
    print(f"Servidor escuchando en {HOST}:{PORT}")
    # Aceptar la conexión entrante
    conn, addr = s.accept()
    with conn:
        print("Conexión establecida desde", addr)
        while True:
            # Recibir datos del cliente
            data = conn.recv(1024)
            if not data:
                break
            print('Mensaje recibido del cliente:', data.decode())
            
            # Extraer la dirección IP del mensaje
            message_parts = data.decode().split('. Ubicación: ')
            if len(message_parts) == 2:
                message = message_parts[0]
                ip = message_parts[1]
                print('Mensaje:', message)
                print('Ubicación:', ip)
                
                # Verificar el mensaje
                if message == expected_message:
                    print("Mensaje recibido correctamente. Iniciando reconocimiento de voz...")
                    
                    # Inicializar el reconocedor
                    r = sr.Recognizer()
                    
                    # Capturar el audio del micrófono
                    with sr.Microphone() as source:
                        print("Por favor, di algo:")
                        audio = r.listen(source)
                    
                        try:
                            # Intentar reconocer el audio usando el reconocedor de Google
                            text = r.recognize_google(audio)
                            print("Creo que dijiste:", text)
                        except sr.UnknownValueError:
                            # El reconocedor no entendió lo que se dijo
                            print("Lo siento, no pude entender el audio.")
                        except sr.RequestError as e:
                            # No se pudo solicitar resultados al servicio de reconocimiento de Google
                            print("No se pudo obtener resultados del servicio de reconocimiento de Google:", e)
                else:
                    print("Mensaje incorrecto. No se iniciará el reconocimiento de voz.")
