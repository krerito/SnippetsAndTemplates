from mysql import mysql
import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host='100.000.000.000',
        database='TestDB',
        user='TestUser',
        password='TestUser'
    )
def update_song(ID_song, songTitle, songLyrics, songRelation):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = 'UPDATE TestKerim SET songTitle = %s, songLyrics = %s, songRelation = %s WHERE ID_song = %s'
    values = (songTitle, songLyrics, songRelation, ID_song)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
