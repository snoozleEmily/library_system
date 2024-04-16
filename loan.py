from dash import *
from fetch_data import *
from not_found_error import *

data = fetch_storage_data()
new_data = update_data(data)

def get_user_data(attribute):
    search_value = input(f"Digite o {attribute}: ")

    # Verifica se é integer ou string
    try:
        search_value = int(search_value)
        data_type = 'CPF' # Define o tipo de dado como CPF
    except ValueError:
        search_value = search_value.lower()
        data_type = 'name' # Define o tipo de dado como Nome

    for user in new_data['users']:
        # Retorna o valor requerido
        if (data_type == 'CPF' and user['CPF'] == search_value) or \
           (data_type == 'name' and user[attribute].lower() == search_value):
            print('Usuário encontrado: ')
            print(user)

            return
    not_found_error(f'{data_type}_value')  


def get_book_data(attribute):
    search_value = input(f"Digite o {attribute.lower()}: ").lower()

    for book in new_data['books']:
        if book[attribute].lower() == search_value:
            print('Livro encontrado:')
            print(book)
            
            return
    not_found_error(f'any_book_value')  #Add msgs de erro diferentes para cada input?

    return book


def loan_book(): #Refatorar esse código para aproveitar o code repetido? 
    print('Pesquisar usuário por: ')
    space()
    print('1) Nome')
    print('2) CPF')
    user_search_type = input('')

    if user_search_type == '1':
        get_user_data('Nome')

    elif user_search_type == '2':
        get_user_data('CPF')


    print('Pesquisar livro por: ')
    space()
    print('1) Nome')
    print('2) Autor')
    print('3) ID')
    book_search_type = input('')
    
    if book_search_type == '1':
        get_book_data('Título')

    elif book_search_type == '2':
        get_book_data('Autor')

    elif book_search_type == '3':
        get_book_data('Número de Identificação')
    
    else:
        print('[ERRO] Escolha uma das opções disponíveis.') 

loan_book()