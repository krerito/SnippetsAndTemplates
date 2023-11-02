from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)
def get_db_connection():
    return mysql.connector.connect(host='',
                                   database='',
                                   user='',
                                   password='')

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'POST':
        ID_song = request.form['ID_song']
        songTitle = request.form['songTitle']
        songLyrics = request.form['songLyrics']
        songRelation = request.form['songRelation']
        
        cursor.execute('INSERT INTO test_table (ID_song, songTitle, songLyrics, songRelation) VALUES (%s, %s, %s, %s)', #cambiar test_table por tabla real
                       (ID_song, songTitle, songLyrics, songRelation))
        conn.commit()
        return redirect('/')
    
    cursor.execute('SELECT * FROM test_table') #cambiar test_table por tabla real
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)