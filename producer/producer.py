import os
import json
import time
from kafka import KafkaProducer

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
TOPIC = "events"

def create_producer():
    return KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

def produce_messages(producer, num_messages=10):
    for i in range(num_messages):
        message = {"id": i, "event": f"Event number {i}"}
        producer.send(TOPIC, message)
        print(f"Sent: {message}")
        time.sleep(1)
    producer.flush()

if __name__ == "__main__":
    producer = create_producer()
    produce_messages(producer)
