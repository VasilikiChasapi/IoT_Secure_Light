import paho.mqtt.client as mqtt
from crypto_utils import encrypt_message, decrypt_message
import config
from logger import log_event

# Dimiourgia MQTT client
client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        log_event("Syndesi sto MQTT broker epitychis!")
        client.subscribe(config.MQTT_TOPIC)
    else:
        log_event(f"Problema syndesis MQTT: {rc}")

def on_message(client, userdata, msg):
    try:
        decrypted = decrypt_message(msg.payload, config.SECRET_KEY)
        log_event(f"Lipsi entolis: {decrypted}")
        # Edo tha kaleitai i logiki gia na allaksei to LED
    except Exception as e:
        log_event(f"Apotuxia apokryptografisis: {e}")
client.on_connect = on_connect
client.on_message = on_message

def start_mqtt():
    client.tls_set()  # Asfalis sindesi me TLS
    client.connect(config.MQTT_BROKER, config.MQTT_PORT)
    client.loop_start()

def send_message(message: str):
    encrypted = encrypt_message(message, config.SECRET_KEY)
    client.publish(config.MQTT_TOPIC, encrypted)
    log_event(f"Apostoli minimatos: {message}")
