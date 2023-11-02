import requests
from flask import Flask, render_template, request, redirect, url_for
from sap import bapicall
app = Flask(__name__)

#Aqui para agarrar mi ip, dunno why
import socket

def get_local_ip():
    try:
        # Crea un socket UDP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Intenta conectarse a una dirección que probablemente no sea local
        # No se enviarán datos
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        print(f"Local IP Address: {ip_address}")
        return ip_address
    except Exception as e:
        print(f"Error obtaining local IP: {e}")
        return None

# Usar la función para obtener la IP local
get_local_ip()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    p_matnr = request.form['P_MATNR']
    response = bapicall(p_matnr)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)