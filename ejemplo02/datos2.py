from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Provincia
from configuracion import engine
Session = sessionmaker(bind=engine)
session = Session()

provincias = session.query(Provincia).all()
# A cada provincia perdile el número de docentes
print("Docentes por provincia")
for provincia in provincias:
    print("Provincia: %s" % (provincia.nombre))
    print("Numero docentes: %s" % (provincia.obtenerNumDocentes()))


session.close()
