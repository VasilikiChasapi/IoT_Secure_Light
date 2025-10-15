import logging

# Aplos logger gia na deixnei ti ginetai
logging.basicConfig(
    filename='device.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_event(event: str):
    print(event)
    logging.info(event)
