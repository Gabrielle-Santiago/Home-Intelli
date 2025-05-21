import os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt

load_dotenv()

MQTT_HOST = os.getenv("MQTT_HOST") or "localhost"
MQTT_PORT = int(os.getenv("MQTT_PORT") or 1883)
MQTT_TOPIC = os.getenv("MQTT_TOPIC") or "test/topic"


def publish_message(message: str):
    client = mqtt.Client()
    client.connect(MQTT_HOST, MQTT_PORT, 60)
    client.publish(MQTT_TOPIC, message)
    client.disconnect()