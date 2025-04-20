import sqlite3
import random
from datetime import datetime, timedelta

# Connect to the MariaDB database
conn = sqlite3.connect('../chinook_test.db')
cursor = conn.cursor()

# Function to generate random department
def generate_department():
    departments = ['HR', 'Engineering', 'Marketing', 'Sales', 'Finance', 'IT']
    return random.choice(departments)

# Function to generate random position
def generate_position():
    positions = ['Manager', 'Developer', 'Analyst', 'Consultant', 'Specialist']
    return random.choice(positions)

# Function to generate random salary
def generate_salary():
    return round(random.uniform(30000, 150000), 2)

# Function to generate random hire date
def generate_hire_date(start_year=2000, end_year=2023):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randrange(delta.days)
    return start_date + timedelta(days=random_days)

create_table_query = '''
CREATE TABLE IF NOT EXISTS humanresource (
    primaryKey integer PRIMARY KEY AUTOINCREMENT,
    user_id integer,
    department text,
    position text,
    salary integer,
    hire_date date
)
'''

cursor.execute(create_table_query)



# Insert 1,000,000 random entries
for _ in range(10000):
    user_id = random.randint(1, 100)
    department = generate_department()
    position = generate_position()
    salary = generate_salary()
    hire_date = generate_hire_date()
    cursor.execute("""
        INSERT INTO humanresource (user_id, department, position, salary, hire_date)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, department, position, salary, hire_date))

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()

print("Inserted 100,000 rows into the 'humanresource' table.")
