from mysql import mysql
import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host='100.000.000.000',
        database='TestDB',
        user='TestUser',
        password='TestUser'
    )
def delete_song(ID_song):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = 'DELETE FROM TestKerim WHERE ID_song = %s'
    cursor.execute(query, (ID_song,))
    conn.commit()
    cursor.close()
    conn.close()
