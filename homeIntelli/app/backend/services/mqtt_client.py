import os
import paho.mqtt.client as mqtt

from dotenv import load_dotenv
from core.mqtt_handle import handle_message

load_dotenv()

# def get_env(var_name: str) -> str:
#     value = os.getenv(var_name)
#     if value is None:
#         raise EnvironmentError(f"Environment variable '{var_name}' is not defined.")
#     return value

MQTT_HOST = os.getenv("MQTT_HOST") or "localhost"
MQTT_PORT = int(os.getenv("MQTT_PORT") or 1883 ) 
MQTT_TOPIC = os.getenv("MQTT_TOPIC") or "home/temperature"

def on_connect(client, userdata, flags, rc):
    print(f"MQTT connected: {str(rc)}")
    for topic, _ in MQTT_TOPIC:
        client.subscribe(topic)
        print(f"Subscribe to: {topic}")

def on_message(client, userdata, msg):
    handle_message(msg.topic, msg.payload.decode())

def start_mqtt():
    client = mqtt.Client()
    client.username_pw_set(os.getenv("MQTT_USERNAME"), os.getenv("MQTT_PASSWORD"))
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_HOST, MQTT_PORT, 60)
    client.loop_start()