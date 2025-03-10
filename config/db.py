import sqlite3

def init_db():
  try:
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )'''
    )

  except Exception as e:
    print(f"Error occured while init db : {e}")
  else:
    print("db initialized succesfully")

  finally:
    conn.commit()
    conn.close()
