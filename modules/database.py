import sqlite3

# Connect to database
conn = sqlite3.connect("database/defect_tracker.db")

# Create cursor
cursor = conn.cursor()

print("Database connected successfully")