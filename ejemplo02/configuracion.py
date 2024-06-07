from sqlalchemy import create_engine
# se genera en enlace al gestor de base de
# datos
# mysql
# pip install mysql-connector-python
#engine = create_engine('mysql+mysqlconnector://root:@localhost/final1bim')

cadena_base_datos = 'sqlite:///base001.db' 

engine = create_engine(cadena_base_datos)