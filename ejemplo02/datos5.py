from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Parroquia
from configuracion import engine
Session = sessionmaker(bind=engine)
session = Session()

parroquias = session.query(Parroquia).all()
#  A cada parroquia preguntarle los tipos jornada de los establecimientos
print("Tipos de jornada por parroquias")
for parroquia in parroquias:
    print("Parroquia: %s" % (parroquia.nombre))
    print("Tipos de jornada: %s" % (parroquia.tiposJornada()))
    print("-"*50)

session.close()
