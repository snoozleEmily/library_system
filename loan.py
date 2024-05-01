from dash import *
from get_data import *
from error import *

def make_loan(user, book):
    
     # Verifica se o usuário já está com um livro emprestado
    if 'borrowed_book' in user and user['borrowed_book']:
        found_error('unavailable_user')
        print('Livro: ', user['borrowed_book'])
        print('Deseja realizar devolução?')
        print('1) SIM')
        print('2) NÃO, VOLTAR PARA O MENU')

        # CHAMAR A FUNÇÃO DE DEVOLUÇÃO AQUI
        return
    
    else:
        for lending_book in data['books']: # Atualiza o número de copias disponíveis
            if lending_book['Número de Identificação'] == book['Número de Identificação']:

                if lending_book['Copias Disponíveis'] == 0:
                    found_error('unavailable_book')
                    return
                
                lending_book['Copias Disponíveis'] -= 1
                break
        
        # Atualiza os dados usuário registrando o empréstimo
        for user_data in data['users']:
            if user_data['Nome'] == user['Nome'] or user_data['CPF'] == user['CPF']:
                # Atualiza borrowed_book para o user
                user['borrowed_book'] = {
                    'Título': book['Título'],
                    'ID': book['Número de Identificação']}
                
                user_data.update(user)
                break

        print("Emprestado:", book["Título"], "para", user["Nome"])
        print("Copias Disponíveis atualizadas:", lending_book['Copias Disponíveis'])

        save_data(data)

def loan_book():
    
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


    make_loan(user, book)

loan_book()