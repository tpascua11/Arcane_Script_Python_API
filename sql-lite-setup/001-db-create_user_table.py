import sqlite3
import hashlib
import os  # Import for generating random salt

conn = sqlite3.connect("game_world.db")
cur = conn.cursor()

# Create the table with secure password storage
cur.execute("""
CREATE TABLE IF NOT EXISTS game_world(
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    salt BLOB NOT NULL  -- Column for password salt
)
""")

conn.commit()
conn.close()