from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Parroquia
from configuracion import engine
Session = sessionmaker(bind=engine)
session = Session()

parroquias = session.query(Parroquia).all()
# A cada parroaquia preguntar el número de establecimientos
print("Establecimientos por parroquia")
for parroquia in parroquias:
    print("Parroquia: %s" % (parroquia.nombre))
    print("Numero establecimientos: %s" % (parroquia.numEstablecimientos()))


session.close()
