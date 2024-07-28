import uuid
from typing import Union, Callable

from dash import dash, space
from error import found_error, get_current_year
from fetch_data import pd, books_df, save_books

# Declarando variável global
_single_book: dict = {}   

#Cadastro de Livros: título, autor, ano da publicação, quantidade de cópias disponíveis em estoque e as emprestadas
class Book:
    def __init__(self, title, author, publish_year, copies_in_stock, copies_available):
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.copies_in_stock = copies_in_stock        
        self.copies_available = copies_available

def create_book() -> Union[dict, Callable[[pd.DataFrame], pd.DataFrame]]:
    current_year= get_current_year()
    title = input('Título do livro: ')
    author = input('Autor do livro: ')
    
    numeric_input_prompts = [
        ('Ano de publicação do livro', 'publish_year'),
        ('Cópias em Estoque', 'copies_in_stock'),
        ('Cópias Disponíveis', 'copies_available')
    ]

    # Garante que os inputs numerais estão corretos
    for prompt, attribute in numeric_input_prompts:
        while True:
            type_input = input(f'{prompt}: ')
            error_type = 'invalid_value' # Determina erro padrão

            try:
                match attribute:
                    case 'publish_year':
                        publish_year = int(type_input)

                        if len(type_input) != 4:
                            # Levanta um erro caso o input não tenha 4 digitos
                            error_type = 'year_length'
                            raise ValueError
                        if int(type_input) > current_year:
                            # Levanta um erro caso o input seja maior do que o ano atual
                            error_type = 'year_current'
                            raise ValueError
                        
                    case 'copies_in_stock':
                        copies_in_stock = int(type_input) 
                        
                    case 'copies_available':
                        copies_available = int(type_input)
                        stock_amount = copies_in_stock #Guarda o valor de copies_in_stock como integer

                        if stock_amount < copies_available:
                            # Número de cópias disponíveis não pode ser maior do que cópias em estoque
                            error_type = 'exceeded_book_limit'        
                            raise ValueError 
                        
                        elif stock_amount > copies_available:
                            found_error('missing_user')  
                                                    
                        copies_in_stock = []         
                        availability_count = 0 # Rastreia o número de cópias disponíveis
                        
                        for _ in range(stock_amount):
                            # Verifica se cada cópia está disponível para empréstimo
                            is_available = True if availability_count != copies_available else False

                            # Gera uma ID aleatória para a cópia e a adiciona à lista de livros disponíveis
                            copy_id =  str(uuid.uuid4()) 
                            copies_in_stock.append({'ID': copy_id, 'Disponível': is_available})
                            
                            # Incrementa o contador de cópias disponíveis se a cópia estiver disponível para empréstimo
                            if is_available:                                
                                availability_count += 1                                                                
                break
            except ValueError:
                found_error(error_type)

    # Passa as informações da classe Book para uma variável
    new_book = Book(title, author, publish_year, copies_in_stock, copies_available)

    global _single_book
    _single_book = {
        'Título': new_book.title,
        'Autor': new_book.author,
        'Ano de Publicação': new_book.publish_year,
        'Copias em Estoque': new_book.copies_in_stock,
        'Copias Disponíveis': new_book.copies_available
        }    
    return _single_book and add_new_book(books_df)

def add_new_book(books_df: pd.DataFrame) -> pd.DataFrame:
    new_book_df = pd.DataFrame([_single_book])        
    updated_books_df = pd.concat([books_df, new_book_df], ignore_index=True)
    space()
    dash()
    print('Adicionar PERMANETEMENTE os seguintes dados?')
    dash()
    print(_single_book)

    space()
    print('1.SIM | 2.NÃO')
    correct_input = input()    
    match correct_input:         
        case '1':
            # Salva os dados do novo livro permanentemente no armazenamento
            save_books(updated_books_df)
            print('Livro Registrado Com Sucesso!')                             
        case '2':
            print('1) Menu principal')
            print('2) Inserir dados novamente')
            
            redo_input = input()
            match redo_input:
                case '1':
                    _single_book.clear()                   
                    pass
                case '2':
                    create_book()
        case _ :
            found_error('invalid_value')
            correct_input = input('1.SIM | 2.NÃO')
            space()

    _single_book.clear()
    return updated_books_df

if __name__ == '__main__':
    create_book()