import os
import json
from kafka import KafkaConsumer

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
TOPIC = "events"

def create_consumer():
    return KafkaConsumer(
        TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        auto_offset_reset='earliest',
        api_version =(0,11,5),
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

def consume_messages(consumer, max_messages=10):
    count = 0
    for message in consumer:
        print(f"Received: {message.value}")
        count += 1
        if count >= max_messages:
            break

if __name__ == "__main__":
    consumer = create_consumer()
    consume_messages(consumer)
