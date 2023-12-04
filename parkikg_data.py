import time
import json
import random  # Add this line
from confluent_kafka import Producer

# Kafka configuration
kafka_bootstrap_servers = 'localhost:9092'
kafka_topic = 'parking_data'

# Create Kafka producer configuration
producer_config = {
    'bootstrap.servers': kafka_bootstrap_servers,
}

# Create Kafka producer
producer = Producer(producer_config)

# Function to generate continuous real-time data
def generate_real_time_data():
    while True:
        timestamp = int(time.time())
        occupancy_data = {'timestamp': timestamp, 'occupancy': {}}

        # Simulate parking space occupancy
        for space in range(1, 101):  # Assuming 100 parking spaces
            occupancy_data['occupancy'][str(space)] = 1 if random.randint(0, 1) == 1 else 0

        # Convert data to JSON
        json_data = json.dumps(occupancy_data)

        # Produce the message to the Kafka topic
        producer.produce(kafka_topic, value=json_data)

        # Wait for a short interval before sending the next message
        time.sleep(0)  # Adjust the sleep interval based on your requirements

# Start generating real-time data
generate_real_time_data()
