import json
import unittest
from producer import create_producer

class TestProducer(unittest.TestCase):
    def test_value_serializer(self):
        producer = create_producer()
        # Simulate serialization
        value = {"test": "value"}
        serialized = producer.config['value_serializer'](value)
        # Check that the output is in JSON bytes
        self.assertEqual(json.loads(serialized.decode('utf-8')), value)

if __name__ == '__main__':
    unittest.main()
