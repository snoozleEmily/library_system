import uuid
from dash import *
from fetch_data import *
from error import *

#Cadastro de Livros: título, autor, ano da publicação, quantidade de cópias disponíveis em estoque e as emprestadas
class Book:
    def __init__(self, title, author, publish_year, copies_available, copies_in_stock):
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.copies_available = copies_available
        self.copies_in_stock = copies_in_stock

single_book = {} #Criando variável global     
def create_book():
    title = input('Título do livro: ')
    author = input('Autor do livro: ')
    
    # Variáveis locais para armazenar os valores dos inputs
    publish_year = None
    copies_in_stock = None
    copies_available = None

    numeric_input_prompts = [
        ('Ano de publicação do livro', 'publish_year'),
        ('Cópias em Estoque', 'copies_in_stock'),
        ('Cópias Disponíveis', 'copies_available')
    ]

    # Garante que os inputs numerais estão corretos
    for prompt, attribute in numeric_input_prompts:
        while True:
            user_input = input(f'{prompt}: ')
            error = 'invalid_value'

            try:
                if attribute == 'publish_year':
                    publish_year = int(user_input)

                    if len(user_input) != 4:
                        error = 'year_length'
                        raise ValueError
                    if int(user_input) > current_year:
                        error = 'year_current'
                        raise ValueError
                    
                if attribute == 'copies_in_stock':
                    copies_in_stock = int(user_input) 
                    
                if attribute == 'copies_available':
                    copies_available = int(user_input)

                    if copies_in_stock < copies_available:
                        error = 'exceeded_book_limit'
                        raise ValueError
                    
                    copies_available = []
                    for _ in range(copies_in_stock):
                        # Gera uma ID aleatória
                        id =  str(uuid.uuid4()) 
                        copies_available.append({'ID': id, 'Disponível': True}) # Preciso checar se cada unidade está disponível - ao invés de todas serem True
                        
                break
            except ValueError:
                found_error(error)

    # Passando as informações da classe Book para uma variável
    new_book = Book(title, author, publish_year, copies_in_stock, copies_available)

    global single_book
    single_book = {
        'Título': new_book.title,
        'Autor': new_book.author,
        'Ano de Publicação': new_book.publish_year,
        'Copias em Estoque': new_book.copies_in_stock,
        'Copias Disponíveis': new_book.copies_available
        }
    #found_error('missing_user')  I should look if there is a user with this book loaned in case copies_available < copies_in_stock
    return single_book and add_new_book()

def add_new_book():
    books_data = fetch_storage_data()
    space()
    
    print('Adicionar PERMANETEMENTE os seguintes dados?')
    print(single_book)

    space()
    print('1.SIM | 2.NÃO')
    correct_input = input()

    if correct_input not in ['1', '2']:
        print('[ERRO] Escolha uma das opções disponíveis.')
        correct_input = input('1.SIM | 2.NÃO')
    
    # Salvar os dados do novo livro permanentemente no armazenamento 
    if correct_input == '1': 
        books_data['books'].append(single_book) 
        save_data(books_data)
        print('Livro Registrado Com Sucesso!')

    # Corrigir os dados do novo livro 
    if correct_input == '2':
        create_book()

    return books_data

create_book()