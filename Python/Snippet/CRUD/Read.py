from mysql import mysql
import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host='100.000.000.000',
        database='TestDB',
        user='TestUser',
        password='TestUser'
    )
def read_songs():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM TestKerim')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
