from peewee import *

# Conexión a SQLite (solo un archivo, sin servidor)
db = SqliteDatabase('tareas.db')

class BaseModel(Model):
    class Meta:
        database = db

class Tarea(BaseModel):
    titulo = CharField()
    descripcion = TextField()
    completada = BooleanField(default=False)

    class Meta:
        table_name = 'tareas'

# Crear la tabla si no existe
def inicializar():
    db.connect(reuse_if_open=True)
    db.create_tables([Tarea])