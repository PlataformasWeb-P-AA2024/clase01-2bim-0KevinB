from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Canton
from configuracion import engine
Session = sessionmaker(bind=engine)
session = Session()

cantones = session.query(Canton).all()
# A cada cantón pedirle el número de estudiantes
print("Estudiantes por canton")
for canton in cantones:
    print("Canton: %s" % (canton.nombre))
    print("Numero estudaintes: %s" % (canton.obtenerNumEstudaintes()))


session.close()
