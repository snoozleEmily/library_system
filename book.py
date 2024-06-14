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

 # Declarando variável global
_single_book = {}   
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
            error = 'invalid_value' # Determina erro padrão

            try:
                match attribute:
                    case 'publish_year':
                        publish_year = int(type_input)

                        if len(type_input) != 4:
                            # Levanta um erro caso o input não tenha 4 digitos
                            error = 'year_length'
                            raise ValueError
                        if int(type_input) > current_year:
                            # Levanta um erro caso o input seja maior do que o ano atual
                            error = 'year_current'
                            raise ValueError
                        
                    case 'copies_in_stock':
                        copies_in_stock = int(type_input) 
                        
                    case 'copies_available':
                        copies_available = int(type_input)
                        stock_amount = copies_in_stock #Guarda o valor de copies_in_stock como integer

                        if stock_amount < copies_available:
                            # Levanta um erro caso o número de cópias disponíveis seja maior do que cópias em estoque
                            error = 'exceeded_book_limit'        
                            raise ValueError                    
                        
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
            all_books_and_users_data['books'].append(_single_book) 
            save_data(all_books_and_users_data)
            print('Livro Registrado Com Sucesso!')
            '''
            # Retorna quantas copias estão disponíveis 
            for copy in _single_book['Copias Disponíveis']:
                avaliable_copies = 0
                if copy['Disponível'] == True:
                    avaliable_copies += 1            

            # Verifica se a quantidade de livros em estoque é a mesma dos disponíveis
            if _single_book['Copias em Estoque'] == avaliable_copies:
                pass
            else:
                found_user = False
                for user in data['users']:
                    try:
                        if user['Livro Em Posse']['Título'] == _single_book['Título']:
                           print('Encontrei alguém com uma cópia desse livro já emprestada, mas ainda não foi resgistrado. Deseja atualizar o usuário?')
                           update_choice = input('1.SIM | 2.NÃO')
                           space()
                           match update_choice:
                                case '1':
                                    borrow_book_id = _single_book['Copias em Estoque']['ID']
                                    print(borrow_book_id)
                                    found_user = True
                                case '2':
                                   break #Skipa todo o código restante e finaliza
                    except (AttributeError, KeyError, TypeError): #Pq tô usando isso aqui?
                        pass   

                if not found_user:
                    found_error('missing_user')
             '''       
        case '2':
            print('1) Menu principal')
            print('2) Inserir dados novamente')
            
            redo_input = input()
            match redo_input:
                case '1':
                    # Volta para o menu principal
                    pass
                case '2':
                    # Corrigi os dados do novo livro
                    create_book()
        case _ :
            print('[ERRO] Escolha uma das opções disponíveis.')
            correct_input = input('1.SIM | 2.NÃO')
            space()

    return all_books_and_users_data