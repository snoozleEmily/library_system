from dash import *
from fetch_data import *
from error import *

def get_user_data(attribute):
        # Guarda o input na variável search_value
        search_value = input(f"Digite o {attribute}: ")
        error_type = 'invalid_value' # Define erro padrão
        
        if attribute == 'Nome':
            error_type = 'name'
        elif attribute == 'CPF':
            try:
                if len(search_value) != 11: #TÁ DANDO PROBLEMA AQUI?
                    # Se o CPF não tive 11 digitos, exibe um erro
                    found_error('cpf_length')

                # Converte o input do CPF em integer    
                search_value = int(search_value)
                error_type = 'CPF'

            except ValueError:  
                # Se o input do CPF não for um número, exibe um erro
                found_error(error_type)
                ask_user_input()
                return
        else:
            # Se o input for desconhecido, exibe um erro
            found_error(f'invalid_{error_type}')
            ask_user_input()

        for user in all_books_and_users_data['users']:
            if user[attribute] == search_value:
                print('Usuário: ')
                print(user)
                space()
                return user
            
         # Se o usuário não for encontrado, exibe um erro  
        found_error(f'invalid_{error_type}')
        ask_user_input()
    
def ask_user_input():
        print('Pesquisar usuário por: ')
        space()
        print('1) Nome')
        print('2) CPF')
        # Guarda o input na variável user_search
        user_search = input('') 
        match user_search:
            case '1':
                user = get_user_data('Nome')
                return user
            case '2':
                user = get_user_data('CPF')
                return user
            case _:
                # Se o input não for '1' ou '2', exibe um erro
                found_error('invalid_value') 
                ask_user_input()
        
   
def get_book_data(attribute):
        # Guarda o input na variável search_value
        search_value = input(f"Digite o {attribute}: ") 
        
        for book in all_books_and_users_data['books']:
            if book[attribute].lower() == search_value.lower():
                print('Livro: ')
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
        # Guarda o input na variável book_search
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
                # Se o input não for '1', '2' ou '3', exibe um erro
                found_error('invalid_value') 
                ask_book_input()        