# Importamos nuestra librearia de graficas que nos hace un chambononon
import matplotlib.pyplot as plt

#importamos pyobdc para poder crear hacer la conexion a nuestra base de datos
import pyodbc

# Estan son variables porque el ttiempo y el como se hace la traduccion fue un caos
from datetime import datetime, date, timedelta

# Convertir a HTML
import mpld3


# Conexión a la base de datos
connection = pyodbc.connect('DRIVER={SQL Server};SERVER=;DATABASE=;UID=sa;PWD=!')

# Obtener la fecha actual
current_date = date.today()

def update_graph(machine_id):

# Ejecutar la consulta para el día actual y la máquina con ID 4
    query = f"""
    SELECT
        Time,
        Status
    FROM
        mdetail
    WHERE
        date = '{current_date}'
        AND MachineId = {machine_id}
    ORDER BY
        Time
    """

    cursor = connection.cursor()
    cursor.execute(query)

    # Procesar los resultados
    segments = []

    for row in cursor.fetchall():
        time = row.Time  # Mantener el objeto datetime completo
        status = row.Status
        segments.append((time, status))

    # Cierre de la conexión a la base de datos
    connection.close()

    # Creación de la gráfica de Gantt
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.set_ylim(-0.5, 0.5)

    start_time = datetime.combine(current_date, datetime.min.time())
    end_time = datetime.combine(current_date, datetime.max.time())
    prev_status = None
    for segment in segments:
        time, status = segment
        if prev_status is not None:
            duration = (time - start_time).seconds / 3600  # Convertir a horas
            color = 'green' if prev_status == 'Run' else ('yellow' if prev_status == 'Stop' else ('red' if prev_status == 'Alarm' else 'black'))
            ax.barh(0, duration, left=(start_time - datetime.combine(current_date, datetime.min.time())).seconds / 3600, height=0.2, color=color)
            start_time = time
        prev_status = status

        # Añadir segmento azul para espacios vacíos
        if time > end_time:
            duration = (time - end_time).seconds / 3600
            ax.barh(0, duration, left=(end_time - datetime.combine(current_date, datetime.min.time())).seconds / 3600, height=0.2, color=color)
        end_time = time

    # Agregar el último segmento
    if prev_status is not None:
        duration = (end_time - start_time).seconds / 3600
        color = 'green' if prev_status == 'Run' else ('yellow' if prev_status == 'Stop' else ('red' if prev_status == 'Alarm' else 'black'))
        ax.barh(0, duration, left=(start_time - datetime.combine(current_date, datetime.min.time())).seconds / 3600, height=0.2, color=color)

    plt.yticks([0], [current_date.strftime('%Y-%m-%d')])
    plt.xticks(range(0, 24))
    plt.xlabel('Hora del Día')
    plt.ylabel('Fecha')
    plt.title(f'Utilización de la maquinaria (ID {machine_id}) el {current_date}')
    plt.tight_layout()
    #Lo mostramos
    #plt.show()

    #Lo mostramos
    #mpld3.show(fig)

    # Transformamos el grafico a d3.js
    interactive_graph = mpld3.fig_to_html(fig)
    return interactive_graph