from flask import Flask, render_template
from ctx3_Live import update_graph

app = Flask(__name__)



@app.route('/')
def index():
    machine_id = 4
    graph_html = update_graph(machine_id)
    return render_template('index.html', graph_html=graph_html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)