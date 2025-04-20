import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect('../chinook_test.db')
cursor = conn.cursor()

# Function to generate random text content
def generate_content():
    words = ["Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"]
    return " ".join(random.choices(words, k=10))

# Function to generate a random timestamp
def generate_timestamp(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

# Define the start and end times for the random timestamp
start_time = datetime.now() - timedelta(days=365)  # 1 year ago
end_time = datetime.now()

# Insert 1,000,000 random documents into the texts collection
create_table_query = '''
CREATE TABLE IF NOT EXISTS text_document (
    primaryKey integer PRIMARY KEY AUTOINCREMENT,
    user_id integer,
    content text,
    timestamp timestamp
)
'''

cursor.execute(create_table_query)

for _ in range(100000):
    user_id = random.randint(1, 100)
    content = generate_content()
    timestamp = generate_timestamp(start_time, end_time)
    cursor.execute("""
        INSERT INTO text_document (user_id, content, timestamp)
        VALUES (?, ?, ?)
    """, (user_id, content, timestamp))

conn.commit()

# Close the connection
cursor.close()
conn.close()

print("Inserted 1,000,000 documents into the 'texts' collection.")
