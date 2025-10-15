from network import start_mqtt, send_message
from logger import log_event
import time

# Arxikopoihsh MQTT
start_mqtt()

# Apla LED status
LED_STATUS = False

def toggle_led():
    global LED_STATUS
    LED_STATUS = not LED_STATUS
    status = "ON" if LED_STATUS else "OFF"
    log_event(f"LED: {status}")
    # Edo vazoume ton kwdika gia na anapsei/svisei to LED me GPIO
    # gia dokimes mporei na ektupwnei mono

# Kyprio loop
try:
    while True:
        # Stile entoli gia dokimes
        send_message("toggle_led")
        toggle_led()
        time.sleep(10)
except KeyboardInterrupt:
    log_event("Syskevi stamatise.")