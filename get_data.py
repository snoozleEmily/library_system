from dash import *
from fetch_data import *
from error import *

data = fetch_storage_data()

def get_user_data(attribute): 
    search_value = input(f"Digite o {attribute}: ")

    # REFATORAR ESSA PARTE AQUI
    try:
        search_value = int(search_value)
        data_type = 'CPF' # Define o tipo de dado como CPF
    except ValueError:
        search_value = search_value.lower()
        data_type = 'name' # Define o tipo de dado como Nome

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