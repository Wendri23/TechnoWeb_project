import sqlite3

def init_db():
    try:
        conn = sqlite3.connect('config/database.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
    except Exception as e:
        print(f"Erreur lors de l'initialisation de la DB : {e}")
    else:
        print("DB initialisee avec succes")
    finally:
        conn.commit()
        conn.close()
        
def add_user(username, email, password):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (username, email, password)
            VALUES (?, ?, ?)
        ''', (username, email, password))
    except Exception as e:
        print(f"Erreur lors de l'ajout de l'utilisateur : {e}")
    else:
        print("Utilisateur ajoute avec succes")
    finally:
        conn.commit()
        conn.close()

def get_user(user_id):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, username, email, password
            FROM users
            WHERE id = ?
        ''', (user_id,))
        user = cursor.fetchone()
        return user
    except Exception as e:
        print(f"Erreur lors de la récupération de l'utilisateur : {e}")
        return None
    finally:
        conn.commit()
        conn.close()