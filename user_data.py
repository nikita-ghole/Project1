import csv
import pandas as pd
from faker import Faker

# Create Faker instance
fake = Faker()

# Generate fake data
data = []
for i in range(1, 101):
    fname = fake.first_name()
    lname = fake.last_name()
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=65).strftime('%Y-%m-%d')
    email = fake.email()
    gender = fake.random_element(elements=('Male', 'Female'))
    address = fake.address()
    age = fake.random_int(min=18, max=65)
    contact = fake.phone_number()
    city = fake.city()
    country = fake.country()

    data.append([i, fname, lname, date_of_birth, email, gender, address, age, contact, city, country])

# Create a DataFrame from the generated data
df = pd.DataFrame(data)

# Save data to xlsx file
excel_file_path = '/home/neosoft/Project1/raw_data.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"Fake data has been generated and saved to {excel_file_path}")

# Save data to CSV file
csv_file_path = '/home/neosoft/Project1/raw_data.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write header
    csv_writer.writerow(['id', 'fname', 'lname', 'date_of_birth', 'email', 'gender', 'address', 'age', 'contact', 'city', 'country'])
    # Write data
    csv_writer.writerows(data)

print(f'CSV file saved to {csv_file_path}')