from fastapi import APIRouter
from services.mqtt_client import publish_message

router = APIRouter()

@router.get("mqtt/test")
def mqtt_test():
    publish_message("Mensagem de teste enviada com FastAPI 🚀")
    return {"status" : "mensagem enviada com sucesso!"}