from flask import Flask, render_template, request, redirect, url_for
from models import Tarea, inicializar

app = Flask(__name__)

# Inicializar la base de datos al arrancar
inicializar()

# ---------- READ (Listar) ----------
@app.route('/')
def index():
    tareas = Tarea.select()
    return render_template('index.html', tareas=tareas)

# ---------- CREATE (Crear) ----------
@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        Tarea.create(titulo=titulo, descripcion=descripcion)
        return redirect(url_for('index'))
    return render_template('crear.html')

# ---------- UPDATE (Editar) ----------
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    tarea = Tarea.get_by_id(id)
    if request.method == 'POST':
        tarea.titulo = request.form['titulo']
        tarea.descripcion = request.form['descripcion']
        tarea.completada = 'completada' in request.form
        tarea.save()
        return redirect(url_for('index'))
    return render_template('editar.html', tarea=tarea)

# ---------- DELETE (Eliminar) ----------
@app.route('/eliminar/<int:id>')
def eliminar(id):
    tarea = Tarea.get_by_id(id)
    tarea.delete_instance()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)