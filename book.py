import uuid
from dash import *
from fetch_data import *

    
class Book:
    def __init__(self, id, title, author, publish_year, copies_available, is_loaned):
        self.id = id 
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.copies_available = copies_available
        self.is_loaned = is_loaned

single_book = {} #Criando variável global     
def create_book():
    id =  str(uuid.uuid4()) # Gera uma ID aleatória
    title = input('Título do livro: ')
    author = input('Autor do livro: ')
    
    # Variáveis locais para armazenar os valores das entradas
    publish_year = None
    copies_available = None
    is_loaned = None

    num_inputs = [
        ('Ano de publicação do livro', 'publish_year'),
        ('Copias em Estoque', 'copies_available'),
        ('Cópias disponíveis para EMPRÉSTIMO', 'is_loaned')
    ]

    # Garantindo que os inputs numerais estão corretos
    for prompt, attribute in num_inputs:
        error = '[ERRO]'
        while True:
            user_input = input(f'{prompt}: ')
            try:
                if attribute == 'publish_year':
                    publish_year = int(user_input)
                    if len(user_input) != 4:
                        error = '[ERRO] O ano precisa ter quatro números.'
                        raise ValueError
                    #if user_input > 2024: #ADD O ANO ATUALIZADO
                    #    error = '[ERRO] Ano inválido.'
                    #    raise ValueError
                    
                elif attribute == 'copies_available':
                    copies_available = int(user_input)

                elif attribute == 'is_loaned':
                    is_loaned = int(user_input)
                    if copies_available >= is_loaned:
                        error = '[ERRO] O número de copias emprestadas não pode ser maior do as copies em estoque.'
                        raise ValueError
                    
                
                break
            except ValueError:
                print(f'{error} O valor apresentado não pode ser aceito. Por favor, digite um NÚMERO válido.')

    # Determinando se o livro está emprestado ou não
    is_loaned = {'Disponível': True, 'Copias Disponíveis': is_loaned} if is_loaned > 0 else {'Disponível': False, 'Copias Disponíveis': is_loaned}

    # Passando as informações da classe Book numa variável
    new_book = Book(id, title, author, publish_year, copies_available, is_loaned)

    global single_book
    single_book = {
            'Número de Identificação': new_book.id,
            'Título': new_book.title,
            'Autor': new_book.author,
            'Ano de Publicação': new_book.publish_year,
            'Copias em Estoque': new_book.copies_available,
            'Empréstimos': new_book.is_loaned
            }
    
    return single_book and add_new_book()

def add_new_book():
    books_data = fetch_storage_data()
    books_data['books'].append(single_book) 
    save_book_data(books_data)

    print('Livro Registrado Com Sucesso! Você adicionou os seguintes dados: ')
    print(single_book)

    return books_data

create_book()