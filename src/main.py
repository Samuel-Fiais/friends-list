import datetime
from time import sleep

from src.DAO.AlwaysDAO import AlwaysDAO
from src.DAO.FriendDAO import FriendDAO
from src.DAO.RemoveDAO import RemoveDAO
from src.DAO.SearchDAO import SearchDAO
from src.DTO.FriendDTO import FriendDTO
from src.DTO.RemoveDTO import RemoveDTO
from src.DTO.SearchDTO import SearchDTO


def main():
    try:
        print("------- Amigos -------")
        while True:
            print("[1] Adicionar Amigo")
            print("[2] Buscar Amigo")
            print("[3] Todos os Amigos")
            print("[4] Remover Amigo")
            print("[5] Sair")
            option = int(input("> "))

            if option == 1:
                nome = input("Nome: ")
                telefone = input("Telefone (xx) x xxxx-xxxx: ")
                print("Nascimento: ")
                dia = int(input("Dia: "))
                mes = int(input("Mês: "))
                ano = int(input("Ano: "))
                nascimento = datetime.datetime(ano, mes, dia)
                friend_dto = FriendDTO(nome, telefone, nascimento)

                friend_dao = FriendDAO()
                res = friend_dao.friend(friend_dto)
                if res:
                    print("Usuário Cadastrado!")
                else:
                    print("Usuário Já Existe!")

            elif option == 2:
                nome = input("Nome: ")
                search_dto = SearchDTO(nome)

                search_dao = SearchDAO()
                res = search_dao.search(search_dto)
                if not res:
                    print("Amigo não encontrado!")
                else:
                    print("---------------------")
                    for data in res:
                        print(f"Amigo: {data[0]}")
                        print(f"Telefone: {data[1]}")
                        print(f"Nascimento: {data[2]}")
                    print("---------------------")
                    sleep(2)

            elif option == 3:
                always_dao = AlwaysDAO()
                res = always_dao.always()
                print("---------------------")
                for data in res:
                    print(f"Amigo: {data[0]}")
                    print(f"Telefone: {data[1]}")
                    print(f"Nascimento: {data[2]}")
                    print("---------------------")
                    sleep(0.2)
                input("Enter: ")

            elif option == 4:
                opt = input("Tem certeza? [S/N] ").upper()[0]
                while opt != "N" and opt != "S":
                    print("Insira uma resposta correta!")
                    opt = input("Tem certeza? [S/N] ").upper()[0]
                if opt == "N":
                    continue
                elif opt == "S":
                    nome = input("Nome: ")
                    remove_dto = RemoveDTO(nome)
                    remove_dta = RemoveDAO()
                    res = remove_dta.remove(remove_dto)
                    if res:
                        print("Amigo Excluído com Sucesso!")
                    else:
                        print("Amigo não Encontrado!")

            elif option == 5:
                print("Encerrado!")
                break

            else:
                continue
    except ValueError:
        print("Um Erro Ocorreu!")
        sleep(1)
        print("Reiniciando...")
        sleep(1)
        main()


main()
