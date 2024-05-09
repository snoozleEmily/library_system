from dash import *
from fetch_data import *
from error import *

def search_data():
    
    def get_user_data(attribute):
        search_value = input(f"Digite o {attribute}: ")
        data_type = 'invalid_value'

        if attribute == 'Nome':
            data_type = 'name'
        elif attribute == 'CPF':
            try:
                search_value = int(search_value)
                data_type = 'CPF'
            except ValueError:  
                # Se o CPF não for um número válido, exibe um erro
                found_error(data_type)
                ask_user_input()
                return
        else:
            # Se o atributo for desconhecido, exibe um erro
            found_error(f'invalid_{data_type}') 
            ask_user_input()

        for user in data['users']:
            if user[attribute] == search_value:
                print('Usuário encontrado:')
                print(user)
                space()
                return user
            
         # Se o usuário não for encontrado, exibe um erro   
        found_error(data_type) 
        ask_user_input()
    
    def ask_user_input():
        print('Pesquisar usuário por: ')
        space()
        print('1) Nome')
        print('2) CPF')
        user_search = input('')

        if user_search == '1':
            user = get_user_data('Nome')
            return user
        elif user_search == '2':
            user = get_user_data('CPF')
            return user
        else:
            # Se o input não for '1' ou '2', exibe um erro
            found_error('invalid_value') 
            ask_user_input()
        
    ask_user_input()

    def get_book_data(attribute):
        search_value = input(f"Digite o {attribute}: ")

        for book in data['books']:
            if book[attribute].lower() == search_value.lower():
                print('Livro encontrado:')
                print(book)
                space()
                return book
            
        # Se o livro não for encontrado, exibe um erro    
        found_error('invalid_book') 
        ask_book_input()
    
    def ask_book_input():
        print('Pesquisar livro por: ')
        space()
        print('1) Nome')
        print('2) ID')
        print('3) Autor')
        book_search = input('')

        if book_search == '1':
            book = get_book_data('Título')
        elif book_search == '2':
            book = get_book_data('Número de Identificação')
        elif book_search == '3':
            book = get_book_data('Autor')    
        else:
            # Se o input não for '1', '2' ou '3', exibe um erro
            found_error('invalid_value') 
            ask_book_input()
        return book
    
    ask_book_input()

search_data()