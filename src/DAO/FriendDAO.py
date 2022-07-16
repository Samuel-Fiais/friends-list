from src.DAO.ConnectDAO import ConnectDAO
from src.DTO import FriendDTO


class FriendDAO(object):
    @staticmethod
    def friend(friend_dto: FriendDTO):
        try:
            conn = ConnectDAO().connect_bd()
            cursor = conn.cursor()
            sql = f'insert into Friends values' \
                  f'("{friend_dto.nome}", "{friend_dto.telefone}", "{friend_dto.nascimento}")'
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except:
            return False
