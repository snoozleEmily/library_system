from dash import *
from fetch_data import *

# Declarando variáveis para cada livro/usuário
individual_book = ''
individual_user = ''

# Declarando listas para todos livros/usuários
all_books = []
all_users = []

def all_users_report():
    for user in data['users']:
        user_name = user['Nome']
        user_id = user['CPF']
        user_info = user['Contato']
        user_loan = user['Livro Em Posse']        

        # Formata as informações de cada usuário e o adiciona à lista de todos os usuários
        individual_user = f'//Nome: {user_name} | CPF: {user_id} | Contato: {user_info} | Livro Em Posse: {user_loan} '
        all_users.append(individual_user)

    # Imprime a lista de todos os usuários    
    for individual_user in all_users:
        dash()
        print(individual_user)
        dash()

def all_books_report():
    for book in data['books']:
        book_title = book['Título']
        book_author = book['Autor']
        book_year = book['Ano de Publicação']
        book_stock = book['Copias em Estoque']
        book_available = book['Copias Disponíveis']

        # Conta o número de cópias em estoque
        copies_stock = 0
        for copy in book_stock: 
          copies_stock += 1   

        # Formata as informações de cada livro e o adiciona à lista de todos os livros
        individual_book = f'//Livro: {book_title} | Autor(a): {book_author} | Ano De Publicação: {book_year} | Copias Em Estoque: {copies_stock} | Copias Disponíveis Para Empréstimo: {book_available} '
        all_books.append(individual_book)

        # Mostra somente os livros disponíveis
        def available_books_report(): #ONDE VOU CHAMAR ISSO? PASSO COMO PARÂMETRO?
            print(f'Em média existem {copies} per book title.')
            if copy['Disponível']:
                print(f'Existem {book_available} livros disponíveis em estoque.')                
                dash()
                print(individual_book)
                dash()
            else:
                print(f'Existem {book_available} livros indisponíveis em estoque.')
        #available_books_report()        

    # Imprime a lista de todos os livros    
    for individual_book in all_books:
        dash()
        #print(individual_book)
        dash()       

all_books_report()

# Relatório Geral
def generate_general_report():
    all_books_report() # Reporte de Livros cadastrados
    all_users_report()

