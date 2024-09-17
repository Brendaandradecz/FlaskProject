import psycopg2
from psycopg2 import OperationalError

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname='flask_project',
            user='postgres',
            password='docemingau',
            host='localhost',
            port='5433'
        )
        return conn
    except OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
