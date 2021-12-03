# Fichero para consultar datos en la DB: fichero_sql_query.py
from sqlalchemy.orm import sessionmaker
from fichero_sql_tablas import Estudiante, create_engine

engine = create_engine('sqlite:///estudiantes.db', echo=True)

# Crea una sesion
Session = sessionmaker(bind=engine)
session = Session()

print('\n')
print('Consultamos todos los registros:')

# Consulta a la base de datos
for estudiante in session.query(Estudiante).order_by(Estudiante.id):
    print(estudiante.nombre, estudiante.apellido1, estudiante.apellido2)

print('\n')
print('Consulta filtrando:')

# Ejemplo filtrar base de datos
for estudiante2 in session.query(Estudiante).filter(Estudiante.universidad == 'UPC'):
    print(estudiante2.nombre, estudiante2.apellido1, estudiante2.apellido2)