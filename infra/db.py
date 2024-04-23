
import sqlite3

def get_db():
    conn = sqlite3.connect('/home/juniordc/Documentos/Faculdade-2024/APS/tp/RPG-Python/main.db')
    cur = conn.cursor()
    return conn,cur

def close_db(conn):
    conn.close()