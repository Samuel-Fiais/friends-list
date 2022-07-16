from src.DAO.ConnectDAO import ConnectDAO
from src.DTO.RemoveDTO import RemoveDTO


class RemoveDAO(object):
    @staticmethod
    def remove(remove_dto: RemoveDTO):
        try:
            conn = ConnectDAO.connect_bd()
            cursor = conn.cursor()
            sql = f'delete from Friends where Nome = "{remove_dto.nome}"'
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except:
            return False
