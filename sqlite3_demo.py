import sqlite3


DB_FILE = "dev.db"

with sqlite3.connect(DB_FILE) as conn:
  print(conn) # <sqlite3.Connection object at 0x7f43314a9990>
  curs = conn.cursor()
  curs.execute("SELECT 'Hello World!'")
  result = curs.fetchone()
  print(result) # ('Hello World!',)
