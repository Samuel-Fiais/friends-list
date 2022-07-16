from src.DAO.ConnectDAO import ConnectDAO


class AlwaysDAO(object):
    @staticmethod
    def always():
        try:
            conn = ConnectDAO.connect_bd()
            cursor = conn.cursor()
            sql = "select * from Friends"
            cursor.execute(sql)
            res = cursor.fetchall()
            return res
        except Exception:
            print(f"Error {Exception}")
            return None