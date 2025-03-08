from flask import Flask,render_template,request,redirect
import mysql.connector
app = Flask(__name__)
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user    ="root",
        password="",
        database="control_tareas"

    )
@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarea2")
    tareas = cursor.fetchall()
    conn.close()
    return render_template('index.html', actividades=tareas)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        actividad = request.form['actividad']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tarea2 (nombre) VALUES (%s)", (actividad,))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('index.html', agregar=True)

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarea2 WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return redirect ("/")
