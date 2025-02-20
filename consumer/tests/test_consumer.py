import json
import unittest
from consumer import create_consumer

class TestConsumer(unittest.TestCase):
    def test_value_deserializer(self):
        consumer = create_consumer()
        # Access the deserializer function from consumer config
        deserializer = consumer.config.get('value_deserializer')
        # Simulate a message payload
        payload = json.dumps({"test": "value"}).encode('utf-8')
        deserialized = deserializer(payload)
        self.assertEqual(deserialized, {"test": "value"})

if __name__ == '__main__':
    unittest.main()
