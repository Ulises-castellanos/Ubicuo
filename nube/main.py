from fastapi import FastAPI, HTTPException
import logging

# Configuración de registro
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/receive_message")
async def receive_message(message: str):
    # Registro del mensaje recibido
    logger.info("Mensaje recibido: %s", message)
    
    # Procesamiento del mensaje
    # Aquí podrías realizar cualquier procesamiento adicional que necesites
    
    # Respuesta
    return {"message_received": message}
