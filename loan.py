from dash import *
from fetch_data import *
from not_found_error import *

data = fetch_storage_data()

def get_user_data(attribute):
    search_value = input(f"Digite o {attribute}: ")

    # Verifica se é integer ou string
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
    not_found_error(f'{data_type}_value')  

def get_book_data(attribute):
    search_value = input(f"Digite o {attribute.lower()}: ").lower()

    for book in data['books']:
        if book[attribute].lower() == search_value:
            print('Livro encontrado:')
            print(book)

            return book
    not_found_error('any_book_value')

def make_loan(user, book):
    # Atualiza o número de copias disponíveis
    for lending_book in data['books']:
        if lending_book['Número de Identificação'] == book['Número de Identificação']:

            if lending_book['Copias Disponíveis'] == 0:
                print("Livro indisponível no momento. Tente novamente mais tarde.")
                return
            
            lending_book['Copias Disponíveis'] -= 1
            break

    # Atualiza borrowed_book para o user
    user['borrowed_book'] = {
        'Título': book['Título'],
        'ID': book['Número de Identificação']
    }

    print("Emprestado:", book["Título"], "para", user["Nome"])
    print("Copias Disponíveis atualizadas:", lending_book['Copias Disponíveis'])

    save_user_data(user)
    save_book_data(book)
    
    

def loan_book(): #Refatorar esse código para aproveitar o code repetido? 
    print('Pesquisar usuário por: ')
    space()
    print('1) Nome')
    print('2) CPF')
    user_search_type = input('')

    if user_search_type == '1':
        user = get_user_data('Nome')
    
    elif user_search_type == '2':
        user = get_user_data('CPF')


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
        print('[ERRO] Escolha uma das opções disponíveis.') 

    make_loan(user, book)


loan_book()