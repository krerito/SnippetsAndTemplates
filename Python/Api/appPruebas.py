#!/usr/bin/env python3

import cgi
import json
import mysql.connector
import datetime

print("Content-Type: application/json\n")

def get_db_connection():
    return mysql.connector.connect(
        host='',
        database='',
        user='',
        password=''
    )

def get_jobs():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM TestTable')  # Ejemplo tabla
    jobs = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # Convert datetime objects to string
    for job in jobs:
        for key, value in job.items():
            if isinstance(value, datetime.datetime):
                job[key] = value.strftime('%Y-%m-%d %H:%M:%S')
    
    return jobs

def application(environ, start_response):
    headers = [('Content-Type', 'application/json'),
               ('Access-Control-Allow-Origin', '*')]
    
    start_response('200 OK', headers)
    jobs = get_jobs()
    return [json.dumps(jobs, indent=4).encode('utf-8')]


jobs = get_jobs()
print(json.dumps(jobs, indent=4))