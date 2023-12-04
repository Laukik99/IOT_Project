from faker import Faker
import time
fake = Faker()

try:
    while True:
        # Generate fake data
        name = fake.name()
        email = fake.email()
        phone_number = fake.phone_number()
        address = fake.address()

        # Print or store the generated data
        print(f"Name: {name}, Email: {email}, Phone: {phone_number}, Address: {address}")

except KeyboardInterrupt:
    print("\nData generation stopped by user.")
