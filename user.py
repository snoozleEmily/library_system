from dash import *
from fetch_data import *
from error import *

single_user = {}

#Cadastro de Usuários: nome, número de identificação (CPF), contato e livro em posse
class User:
    def __init__(self, name, cpf, info):
        self.name = name
        self.cpf = cpf
        self.info = info

def create_user():
    # Variáveis locais para armazenar os valores das entradas
    name = None
    cpf = None
    info = None

    input_prompts = [
        ('Nome completo do usuário', 'name'),
        ('CPF', 'cpf'),
        ('Número de telefone', 'info')
    ]
    
    # Garante que os inputs estão corretos
    for prompt, attribute in input_prompts:
        while True:
            user_input = input(f'{prompt}: ')
            error = 'invalid_value'

            try:
                if attribute == 'name':
                    if user_input == '' or user_input.isdigit():
                        error = 'number_length'
                        raise ValueError
                    name = user_input
                    
                elif attribute == 'cpf':
                    if len(user_input) != 11 or not user_input.isdigit():
                        error = 'number_length'
                        raise ValueError
                    cpf = user_input

                elif attribute == 'info':
                    if len(user_input) != 9 or not user_input.isdigit():
                        error = 'number_length'
                        raise ValueError
                    info = user_input
                break
            except ValueError:
                found_error(error)

    #borrowed_book = input('')  #COMO LIGAR O USER AO BOOK?  Posso chamar loan() aqui?

    # Passando as informações da classe User para uma variável
    new_user = User(name, cpf, info)

    global single_user
    single_user = {
            'Nome': new_user.name,
            'CPF': new_user.cpf,
            'Contato': new_user.info
            }
    
    return single_user and add_new_user()

def add_new_user():
    users_data = fetch_storage_data()
    space()

    print('Adicionar PERMANETEMENTE os seguintes dados?')
    print(single_user)
    
    space()
    print('1.SIM | 2.NÃO')
    correct_input = input()

    if correct_input not in ['1', '2']:
        found_error('invalid_value')
        correct_input = input('1.SIM | 2.NÃO')
    
    # Salva os dados do novo usuário 
    if correct_input == '1': 
        users_data['users'].append(single_user) 
        save_data(users_data)
        print('Usuário Registrado Com Sucesso!')
        # No final colocar opção desse novo usuário fazer um loan dum book

    # Corrigi os dados do novo usuário 
    if correct_input == '2':
        create_user()

    return users_data

create_user()