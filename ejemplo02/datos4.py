from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Provincia
from configuracion import engine
Session = sessionmaker(bind=engine)
session = Session()

provicias = session.query(Provincia).all()
# A cada provincia preguntar la lista de parroquias
print("Lista de parroquias")
for provicias in provicias:
    print("Provincia: %s" % (provicias.nombre))
    print("Lista de parroquias: %s" % (provicias.obtenerListaParroquias()))
    print("-"*50)

session.close()
