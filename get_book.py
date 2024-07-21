from typing import Optional

from dash import space
from fetch_data import pd, books_df
from error import found_error
   
def get_book_data(attribute: str) -> Optional[pd.DataFrame]:
    search_value = input(f"Digite o {attribute}: ") 

    try:    
        for _, row in books_df.iterrows():
            if row.loc[attribute].lower() == search_value.lower():
                print('Livro: ')
                print(row)
                space()
                return row                            
    except: found_error('invalid_book') 

    ask_book_input()
    
def ask_book_input() -> Optional[pd.DataFrame]:
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
            return ask_book_input()   

if __name__ == '__main__':     
    get_book_data('Título')