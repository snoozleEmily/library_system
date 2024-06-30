from dash import *
from fetch_data import *
from error import *

def get_user_data(attribute):
        search_value = input(f"Digite o {attribute}: ")
        error_type = 'invalid_value' # Define erro padrão
        
        if attribute == 'Nome':
            error_type = 'name'
        elif attribute == 'CPF':
            # CPF deve ter 11 digitos
            try: 
                if len(search_value) != 11 and int(search_value):                    
                    found_error('cpf_length')
                else:
                    error_type = 'CPF'
            except ValueError:
                found_error(error_type)
                ask_user_input()
                return
        else:
            found_error(f'invalid_{error_type}')
            ask_user_input()

        for user in all_books_and_users_data['users']:
            if user[attribute] == search_value:
                print('Usuário: ')
                print(user)
                space()
                return user
            
         # Caso o usuário não for encontrado, exibe um erro  
        found_error(f'invalid_{error_type}')
        ask_user_input()
    
def ask_user_input():
        print('Pesquisar usuário por: ')
        space()
        print('1) Nome')
        print('2) CPF')

        user_search = input('') 
        match user_search:
            case '1':
                user = get_user_data('Nome')
                return user
            case '2':
                user = get_user_data('CPF')
                return user
            case _:
                found_error('invalid_value') 
                ask_user_input()
   
def get_book_data(attribute):
        search_value = input(f"Digite o {attribute}: ") 
        
        for book in all_books_and_users_data['books']:
            if book[attribute].lower() == search_value.lower():
                print('Livro: ')
                print(book)
                space()
                return book
            
        # Caso o livro não for encontrado, exibe um erro    
        found_error('invalid_book') 
        ask_book_input()
    
def ask_book_input():
        print('Pesquisar livro por: ')
        space()
        print('1) Nome')
        print('2) ID')
        print('3) Autor')
        
        book_search = input('')
        match book_search:
            case '1':
                book = get_book_data('Título')
                return book
            case '2':
                book = get_book_data('ID')
                return book
            case '3':
                book = get_book_data('Autor')
                return book    
            case _:
                found_error('invalid_value') 
                ask_book_input()        