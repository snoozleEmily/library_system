from dash import *
from fetch_data import *
from error import *

def get_user_data(attribute):
    search_value = input(f"Digite o {attribute}: ")

    # REFATORAR ESSA PARTE AQUI
    try:
        search_value = int(search_value)
        data_type = 'CPF' # Define o tipo do Dado como CPF
    except ValueError:
        search_value = search_value.lower()
        data_type = 'name' # Define o tipo do Dado como Nome

    for user in data['users']:
        # Retorna o valor requerido
        if (data_type == 'CPF' and user['CPF'] == search_value) or \
           (data_type == 'name' and user[attribute].lower() == search_value):
            print('Usuário encontrado: ')
            print(user)

            return user
    found_error(f'invalid_{data_type}')  

def get_book_data(attribute):
    search_value = input(f"Digite o {attribute.lower()}: ").lower()

    for book in data['books']:
        if book[attribute].lower() == search_value:
            print('Livro encontrado:')
            print(book)

            return book
    found_error('invalid_book')

# Add AFTER error handling in case of wrong input or non existing item
def search_data():
    print('Pesquisar usuário por: ')
    space()
    print('1) Nome')
    print('2) CPF')
    user_search_type = input('')

    if user_search_type == '1':
        user = get_user_data('Nome')
    
    elif user_search_type == '2':
        user = get_user_data('CPF')

    else:
        found_error('invalid_value')

    print('Pesquisar livro por: ')
    space()
    print('1) Nome')
    print('2) ID')
    book_search_type = input('')
    
    if book_search_type == '1':
        book = get_book_data('Título')

    elif book_search_type == '2':
        book = get_book_data('Número de Identificação')

    else:
        found_error('invalid_value')
    
    return user, book