from dash import *
from fetch_data import *
from error import *

def get_user_data(attribute: str, users_df: pd.DataFrame) -> pd.Series:
    error_type = 'value' # Define erro padrão    
    search_value = input(f"Digite o {attribute}: ")   
     
    if attribute == 'Nome': error_type = 'name'

    elif attribute == 'CPF':
        # CPF deve ter 11 digitos
        if len(search_value) != 11 and search_value.isdigit():                    
            found_error('cpf_length') 
            
        search_value = int(search_value)
        error_type = 'CPF'

    else: found_error(f'invalid_{error_type}')  
            
    filtered_users = users_df[users_df[attribute] == search_value]

    if not filtered_users.empty:
        print('Usuário encontrado:')
        print(filtered_users)
        space()
        return filtered_users.iloc[0]  # Retorna usuário compatível        
    
    else: # Caso o usuário não for encontrado, exibe um erro 
        found_error(f'invalid_{error_type}')
        ask_user_input(users_df)
    
def ask_user_input(users_df: pd.DataFrame) -> pd.Series:
        print('Pesquisar usuário por: ')
        space()
        print('1) Nome')
        print('2) CPF')

        user_search = input('') 
        match user_search:
            case '1':
                user = get_user_data('Nome', users_df)
                return user
            case '2':
                user = get_user_data('CPF', users_df)
                return user
            case _:
                found_error('invalid_value') 
                ask_user_input(users_df)
   
def get_book_data(attribute: str, books_df: pd.DataFrame) -> pd.Series:
        search_value = input(f"Digite o {attribute}: ") 
        
        filtered_books = books_df[books_df[attribute].str.lower() == search_value.lower()]

        if not filtered_books.empty:
            print('Livro encontrado:')
            print(filtered_books)
            space()
            return filtered_books.iloc[0]  # Retorna livro compatível
                 
        else: # Caso o livro não for encontrado, exibe um erro
            found_error('invalid_book') 
            ask_book_input(books_df)
    
def ask_book_input(books_df: pd.DataFrame) -> pd.Series:
        print('Pesquisar livro por: ')
        space()
        print('1) Nome')
        print('2) ID')
        print('3) Autor')
        
        book_search = input('')
        match book_search:
            case '1':
                book = get_book_data('Título', books_df)
                return book
            case '2':
                book = get_book_data('ID', books_df)
                return book
            case '3':
                book = get_book_data('Autor', books_df)
                return book    
            case _:
                found_error('invalid_value') 
                ask_book_input(books_df)        