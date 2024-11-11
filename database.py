import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname='flask_project1',
        user='postgres',
        password='docemingau',
        host='localhost',
        port='5433',
        options="-c client_encoding=UTF8"
    )
    return conn
try:
    conn = get_db_connection()
    print("Conexão ao banco de dados estabelecida com sucesso!")
    conn.close()
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
