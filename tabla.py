import sqlite3

conexion = sqlite3.connect("tareas.db")
cursor = conexion.cursor()

# Ver todas las tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tablas en la base de datos:")
for t in cursor.fetchall():
    print(" -", t[0])

# Ver el contenido de la tabla 'tareas'
print("\n--- Contenido de 'tareas' ---")
cursor.execute("SELECT * FROM tareas")
for fila in cursor.fetchall():
    print(fila)

conexion.close()