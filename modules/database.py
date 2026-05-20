import sqlite3

# Connect to database
conn = sqlite3.connect("database/defect_tracker.db")

# Create cursor
cursor = conn.cursor()


# ==========================================
# CREATE USERS TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
""")


# ==========================================
# CREATE PROJECTS TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT NOT NULL,
    description TEXT
)
""")


# ==========================================
# CREATE DEFECTS TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS defects (
    defect_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    severity TEXT,
    priority TEXT,
    status TEXT,
    assigned_to TEXT,
    project_name TEXT,
    created_by TEXT,
    created_date TEXT
)
""")

# Save changes
conn.commit()

print("Database and tables created successfully")