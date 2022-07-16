import mysql.connector as mc


# Conecta o banco de dados
class ConnectDAO:
    @staticmethod
    def connect_bd():
        conn = mc.connect(host="", database="", user="", password="")
        if conn.is_connected():
            return conn
        else:
            print("Error!")
            return None
