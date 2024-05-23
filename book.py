import uuid
from dash import *
from error import *
from fetch_data import *

#Cadastro de Livros: título, autor, ano da publicação, quantidade de cópias disponíveis em estoque e as emprestadas
class Book:
    def __init__(self, title, author, publish_year, copies_in_stock, copies_available):
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.copies_in_stock = copies_in_stock        
        self.copies_available = copies_available

_single_book = {} #Declarando variável global     
def create_book():
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
            error = 'invalid_value'

            try:
                match attribute:
                    case 'publish_year':
                        publish_year = int(type_input)

                        if len(type_input) != 4:
                            error = 'year_length'
                            raise ValueError
                        if int(type_input) > current_year:
                            error = 'year_current'
                            raise ValueError
                        
                    case 'copies_in_stock':
                        copies_in_stock = int(type_input) 
                        
                    case 'copies_available':
                        copies_available = int(type_input)
                        copies = copies_available #Guarda o valor de copies_available como integer

                        if copies_in_stock < copies_available:
                            error = 'exceeded_book_limit'        
                            raise ValueError
                        
                        copies_available = []                    
                        available_count = 0 # Rastreia o número de cópias disponíveis
                        
                        for _ in range(copies_in_stock):
                            is_available = True if available_count < copies else False # Verifica se cada cópia está disponível para empréstimo
                            id =  str(uuid.uuid4()) # Gera uma ID aleatória
                            copies_available.append({'ID': id, 'Disponível': is_available})
                            # Caso a cópia esteja disponível o available_count conta +1 livro
                            if is_available:
                                available_count += 1                                                                          
                break
            except ValueError:
                found_error(error)

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
    
    return _single_book and add_new_book()

def add_new_book():
    space()
    print('Adicionar PERMANETEMENTE os seguintes dados?')
    print(_single_book)

    space()
    print('1.SIM | 2.NÃO')
    correct_input = input()  
    if correct_input not in ['1', '2']:
        print('[ERRO] Escolha uma das opções disponíveis.')
        correct_input = input('1.SIM | 2.NÃO')

    match correct_input:         
        case '1':
            # Salva os dados do novo livro permanentemente no armazenamento
            data['books'].append(_single_book) 
            save_data(data)
            print('Livro Registrado Com Sucesso!')

            # Retorna quantas copias estão disponíveis 
            for copy in _single_book['Copias Disponíveis']:
                avaliable_copies = 0
                if copy['Disponível'] == True:
                    avaliable_copies += 1            

            # Verifica se a quantidade de livros em estoque é a mesma dos disponíveis
            if _single_book['Copias em Estoque'] == avaliable_copies:
                print('A quantidade é a mesma!') # O que quero fazer aqui? Só ter um pass ou continue?
            else:
                found_user = False
                for user in data['users']:
                    try:
                        if user['Livro Em Posse']['Título'] == _single_book['Título']:
                           print('We have an user with this book!') #What do I want to do here?
                           found_user = True             

                    except (AttributeError, KeyError, TypeError):
                        pass   

                if not found_user:
                    found_error('missing_user')
                    
        case '2':
            # Corrigi os dados do novo livro
            create_book()

    return data

create_book()