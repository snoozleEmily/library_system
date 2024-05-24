from dash import *
from fetch_data import *
from error import *

 # Declarando variável global
single_user = {}

#Cadastro de Usuários: nome, número de identificação (CPF), contato e livro em posse
class User:
    def __init__(self, name, cpf, info):
        self.name = name
        self.cpf = cpf
        self.info = info

def create_user():
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

            def number_verify():
                # Levanta um erro caso o input não seja numérico
                if not user_input.isdigit():
                    raise ValueError
            try:
                if attribute == 'name':
                    if user_input == '' or user_input.isdigit():
                        # Levanta um erro caso o input seja uma string vazia ou contenha apenas dígitos
                        error = 'number_length'
                        raise ValueError
                    name = user_input

                elif attribute == 'cpf':
                    number_verify()
                    if len(user_input) != 11:
                        # Levanta um erro caso o input não contenha 11 dígitos
                        error = 'cpf_length'
                        raise ValueError
                    cpf = user_input

                elif attribute == 'info':
                    number_verify()
                    if len(user_input) != 9:
                         # Levanta um erro caso o input não contenha 9 dígitos
                        error = 'info_length'
                        raise ValueError
                    info = user_input
                break
            
            except ValueError:
                found_error(error)

    # Passando as informações da classe User para uma variável
    new_user = User(name, cpf, info)

    global single_user
    single_user = {
            'Nome': new_user.name,
            'CPF': new_user.cpf,
            'Contato': new_user.info,
            'Livro Em Posse': ''
            }
    
    return single_user and add_new_user()

def add_new_user():
    space()
    print('Adicionar PERMANETEMENTE os seguintes dados?')
    print(single_user)
    print('1.SIM | 2.NÃO')
    correct_input = input()   

    match correct_input:             
        case '1': 
            # Salva os dados do novo usuário 
            data['users'].append(single_user) 
            save_data(data)
            print('Usuário Registrado Com Sucesso!')        
        case '2':
            # Corrigi os dados do novo usuário 
            create_user()
        case _:
            # Caso o input não seja 1 ou 2 retorna um erro e requere o input novamente
            found_error('invalid_value')
            correct_input = input('1.SIM | 2.NÃO')
    return data