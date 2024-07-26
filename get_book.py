from typing import Optional

from dash import dash, space
from fetch_data import pd, books_df
from error import found_error, get_current_year
   
def display_books(books: pd.DataFrame, header: str = "Livro(s):"):
    print(header)
    for _, row in books.iterrows():
        dash()
        print(row)        

def get_book_data(attribute: str) -> Optional[pd.Series]:
    current_year: int = get_current_year()
    search_value = input(f"Digite o {attribute}: ")
    error_type = 'invalid_value'    
    try:
        if attribute == 'Ano de Publicação':
            search_value = int(search_value)
            year_range = range(search_value - 100, search_value + 101)
            
            if len(str(search_value)) != 4:
                # Levanta um erro caso o input não tenha 4 digitos
                error_type = 'year_length'
                raise ValueError
            if search_value > current_year:
                 # Levanta um erro caso o input seja maior do que o ano atual
                error_type = 'year_current'
                raise ValueError
            
           # Verifica se existe algum livro com o ano exato
            exact_match = books_df[books_df['Ano de Publicação'] == search_value]
            if not exact_match.empty:
                display_books(exact_match, \
                    header="Hurra! Temos o(s) seguinte(s) livro(s) com o ano que você está procurando:")
                return exact_match
            else:
                # Se não houver correspondência exata, exibe livros dentro do intervalo de anos
                similar_books = books_df[books_df['Ano de Publicação'].isin(year_range)]
                if not similar_books.empty:
                    display_books(similar_books, \
                        header="Não há livros com o ano exato, mas temos o(s) seguinte(s) livro(s) dentro do intervalo de anos:")
                else:
                    print('Não foram encontrados livros dentro do intervalo de anos especificado.')
                    
        elif attribute == 'Título': 
            error_type = 'name'
            # Busca por título (case insensitive)
            matching_books = books_df[books_df['Título'].str.lower() == search_value.lower()]
            if not matching_books.empty:
                display_books(matching_books)
            
    except ValueError:
        found_error(f'{error_type}')                
    return None
    
def ask_book_input() -> pd.Series:
    print('Pesquisar livro por: ')
    space()
    print('1) Nome')
    print('2) Autor')
    print('3) Ano de Publicação')
        
    book_search = input('')
    match book_search:
        case '1':
            book = get_book_data('Título')
        case '2':
            book = get_book_data('Autor')
        case '3':
            book = get_book_data('Ano de Publicação')    
        case _:
            found_error('invalid_value') 
            return ask_book_input()
    
    if book is None: 
        found_error('standard')
        return ask_book_input()

    return book

if __name__ == '__main__':     
    ask_book_input()