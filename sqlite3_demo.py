import sqlite3


DB_FILE = "dev.db"

with sqlite3.connect(DB_FILE) as conn:
  print(conn) 
