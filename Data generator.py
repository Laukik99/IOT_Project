import json
import random
from datetime import datetime

# Define vehicle types
vehicle_types = ['bicycle', 'car', 'bike']

# Function to generate vehicle data
def generate_vehicle_data():
    # Randomly choose a vehicle type
    vehicle_type = random.choice(vehicle_types)

    # Generate data based on vehicle type
    if vehicle_type == 'bicycle':
        data = {
            'entry_time': str(datetime.now()),
            'vehicle_type': vehicle_type,
            'owner_name': fake.name(),
            'parking_slot_number': random.randint(1, 100),
            'arrival_time': str(fake.date_time_this_month()),
            'departure_time': str(fake.date_time_this_month()),
            'arrival_date': str(fake.date_this_month())
        }
    else:
        data = {
            'entry_time': str(datetime.now()),
            'vehicle_type': vehicle_type,
            'owner_name': fake.name(),
            'number_plate': fake.license_plate(),
            'parking_slot_number': random.randint(1, 100),
            'arrival_time': str(fake.date_time_this_month()),
            'departure_time': str(fake.date_time_this_month()),
            'arrival_date': str(fake.date_this_month())
        }

    return data

# Initialize Faker
fake = Faker()

# Generate and save vehicle data to JSON file
vehicle_data = []
for i in range(10):
    data = generate_vehicle_data()
    vehicle_data.append(data)

with open('vehicle_data.json', 'w') as f:
    json.dump(vehicle_data, f)

print('Vehicle data saved to vehicle_data.json')
