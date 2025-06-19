import csv
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Define the CSV file name
csv_file = "team_task_allocation_proj/mainApp/ml_models/employee_data.csv"

# Define the column headers
headers = ["name", "skill_level", "experience", "rating", "contributions", "task_allocation"]

# Define possible tasks (customize as needed)
tasks = ["Data Analysis", "Software Development", "Project Management", "Marketing", "Customer Support"]

# Generate 50 entries
with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()  # Write the headers

    for _ in range(50):
        name = fake.name()
        skill_level = random.randint(1, 10)  # Random skill level between 1 and 10
        experience = random.randint(1, 20)  # Random experience between 1 and 20 years
        rating = round(random.uniform(1, 5), 1)  # Random  rating(float) between 1.0 and 5.0
        contributions = random.randint(1, 100)  # Random contributions between 1 and 100
        task_allocation = random.choice(tasks)  # Randomly selected from a predefined list of tasks.

        # Write the row to the CSV file
        writer.writerow({
            "name": name,
            "skill_level": skill_level,
            "experience": experience,
            "rating": rating,
            "contributions": contributions,
            "task_allocation": task_allocation
        })

print(f"Generated 50 entries in {csv_file}")
