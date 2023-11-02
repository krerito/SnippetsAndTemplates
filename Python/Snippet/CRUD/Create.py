from mysql import mysql
import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host='100.000.000.000',
        database='TestDB',
        user='TestUser',
        password='TestUser'
    )

def insert_song(ID_song, songTitle, songLyrics, songRelation):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = 'INSERT INTO TestKerim (ID_song, songTitle, songLyrics, songRelation) VALUES (%s, %s, %s, %s)'
    values = (ID_song, songTitle, songLyrics, songRelation)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
