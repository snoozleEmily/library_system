from typing import Optional

from dash import dash, space
from fetch_data import pd, books_df
from error import found_error, get_current_year
   
def display_books(books: pd.DataFrame, header) -> None:
    print(header)
    
    for _, row in books.iterrows():
        dash()
        print('Livro encontrado: ')
        dash()
        print(f'Nome: ',row.loc['Título'])
        print(f'Autor: ',row.loc['Autor'])
        print(f'Copias Disponíveis: ',row.loc['Copias Disponíveis']\
            if row.loc['Copias Disponíveis'] > 0 else 'Não há copias disponíveis no momento')
        dash()
        space()       

def get_book_data(attribute: str) -> Optional[pd.Series]:
    current_year: int = get_current_year()
    search_value = input(f"Digite o {attribute}: ")
    error_type = 'invalid_value' 
       
    try:
        matching_books = books_df[books_df[attribute].str.lower() == search_value.lower()]
        if not matching_books.empty:
                display_books(matching_books, header='')
                return matching_books.iloc[0]
            
        if attribute == 'Título': error_type = 'name'            
            
        elif attribute == 'Ano de Publicação':          
            if len(str(search_value)) != 4:
                # Levanta um erro caso o input não tenha 4 digitos
                error_type = 'year_length'
                raise ValueError
            if int(search_value) > current_year:
                 # Levanta um erro caso o input seja maior do que o ano atual
                error_type = 'year_current'
                raise ValueError
            
            search_value = int(search_value)
            year_range = range(search_value - 100, search_value + 101) 
            
           # Verifica se existe algum livro com o ano exato
            exact_match = books_df[books_df['Ano de Publicação'] == search_value]
            if not exact_match.empty:
                display_books(exact_match, \
                    header='Temos o(s) seguinte(s) livro(s) com o ano que você está procurando:')
                return exact_match.iloc[0]
            else:
                # Se não houver correspondência exata, exibe livros de anos próximos	
                similar_books = books_df[books_df['Ano de Publicação'].isin(year_range)]
                if not similar_books.empty:
                    display_books(similar_books,\
                        header='Não há livros com esse ano exato, mas temos o(s) seguinte(s) livro(s) aproximados:')
                else:
                    error_type = 'year_unspecified'
                    raise ValueError
            
    except ValueError:
        found_error(f'{error_type}')                
    return None
    
def ask_book_input(year_applicable: bool = True) -> pd.Series:
    book = None
    
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
            if year_applicable:
                book = get_book_data('Ano de Publicação') 
            else:
                found_error('year_unapplicable')   
        case _:
            found_error('invalid_value') 
            return ask_book_input()
    
    # Caso o input seja inválido, solicita novamente
    if book is None: 
        found_error('default')
        return ask_book_input(year_applicable)
    return book

if __name__ == '__main__':     
    ask_book_input()