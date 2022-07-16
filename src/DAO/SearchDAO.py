from src.DAO.ConnectDAO import ConnectDAO
from src.DTO import SearchDTO


class SearchDAO(object):
    @staticmethod
    def search(search_dto: SearchDTO):
        conn = ConnectDAO().connect_bd()
        cursor = conn.cursor()
        sql = f'select * from Friends where Nome = "{search_dto.nome}"'
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        conn.close()
        return res
