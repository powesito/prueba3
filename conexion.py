import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self,
                 host: str = "localhost",
                 user: str = "root",
                 password: str = "",
                 database: str = "veterinaria"):
        self.config = {
            "host": host,
            "user": user,
            "password": password,
            "database": database,
            "autocommit": False
        }
        self.conn = None
        self.cur = None

    def conectar(self):
        """
        Devuelve (cursor, connection). Lanza excepción si falla la conexión.
        """
        try:
            self.conn = mysql.connector.connect(**self.config)
            self.cur = self.conn.cursor(buffered=True)
            return self.cur, self.conn
        except Error as e:
            print(" Error al conectar a la base de datos:", e)
            raise

    def cerrar(self):
        if self.cur:
            self.cur.close()
        if self.conn and self.conn.is_connected():
            self.conn.close()
