from dash import *
from fetch_data import *

#save_user_data(users_data)
new_user = {}

#Cadastro de Usuários: nome, número de identificação (CPF) e contato.
class User:
    def __init__(self, name, cpf, info, borrowed_book):
        self.name = name
        self.cpf = cpf
        self.info = info
        self.borrowed_book = borrowed_book
        
def create_user():
    name = input("Nome completo do usuário: ")

    while True:
        cpf = input("CPF: ")

        if not cpf.isdigit():
            print("[ERRO] O CPF deve conter apenas números")
            continue

        if len(cpf) != 11:
            print("[ERRO] O CPF deve conter 11 dígitos")
            continue
        break
       
    while True: 
        info = input('Número de telefone: ')
        if not info.isdigit():
            print('[ERRO] O número de telefone deve conter apenas números')
            continue
        if len(info) != 9:
            print('[ERRO] O número de telefone celular deve conter 9 dígitos')
            continue
        break 

    borrowed_book = input('')  #COMO LIGAR O USER AO BOOK?  Posso chamar loan() aqui

    global new_user
    new_user = User(name, cpf, info, borrowed_book)

    # Exibe informações sobre o livro recém-adicionado
    space()
    print('Usuário Registrado Com Sucesso!') #erro, nn tá aparecendo

def get_users_list():
    users = get_users_list()
    users.append(new_user)
    print('Você adicionou os seguintes dados: ')
    print(new_user)

    return users


