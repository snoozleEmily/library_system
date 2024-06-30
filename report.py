from dash import *
from fetch_data import *

# Variáveis para armazenar informações de um único livro/usuário
individual_book = ''
individual_user = ''

# Listas para armazenar informações de todos os livros/usuários
all_books = []
all_users = []

def all_users_report():
    # Percorre todos os usuários de storage.json
    for user in all_books_and_users_data['users']:
        user_name = user['Nome']
        user_id = user['CPF']
        user_info = user['Contato']
        user_loan = user['Livro Em Posse']        

        # Formata as informações de cada usuário e o adiciona à lista de todos os usuários
        user_with_loan_checker = f'Nenhum' if user_loan == '' else user_loan
        individual_user = f'//Nome: {user_name} | CPF: {user_id} | Contato: {user_info} | Livro Em Posse: {user_with_loan_checker} '
        all_users.append(individual_user)

    space()
    dash()    
    print('RELATÓRIO COMPLETO DOS USUÁRIOS')
    dash()
    print(f'Há um total de {len(all_users)} usuário(s) cadastrado(s).')

    # Imprime a lista de todos os usuários    
    for individual_user in all_users:
        dash()
        print(individual_user)
        dash()

def all_books_report():
    unavailable_count = 0  # Contador de livros indisponíveis (emprestados)
    quantity_of_titles_stock = 0  #e.g. Título = Orgulho e Preconceito
    sum_of_all_copies = 0  #e.g. Cópias/Exemplares = lista com ID e dispónibilidade (booleano) 
    
    # Percorre todos os livros de storage.json
    for book in all_books_and_users_data['books']:
        book_title = book['Título']
        book_author = book['Autor']
        book_year = book['Ano de Publicação']
        book_stock = book['Copias em Estoque']
        book_available = book['Copias Disponíveis']
        
        copies_stock = len(book_stock)   
        unavailable_count += sum(1 for copy in book_stock if not copy['Disponível'])           

        # Formata as informações de cada livro e o adiciona à lista de todos os livros
        individual_book = f'//Livro: {book_title} | Autor(a): {book_author} | Ano De Publicação: {book_year} | Copias Em Estoque: {copies_stock} | Copias Disponíveis Para Empréstimo: {book_available} '
        all_books.append(individual_book)    

        # Conta a quantidade de livros em estoque
        quantity_of_titles_stock = len(all_books_and_users_data['books'])
        sum_of_all_copies += copies_stock 
    
    # Imprime a quantidade total de livros em estoque
    space()
    dash()  
    print('RELATÓRIO COMPLETO DOS LIVROS')
    dash()
    print(f'Há um total de {quantity_of_titles_stock} títulos e {sum_of_all_copies} exemplares em estoque')

    # Imprime a quantidade de livros emprestados e a média de cópias por título
    if unavailable_count != 0:
        copies_mean = sum_of_all_copies/quantity_of_titles_stock 
        print(f'Há {unavailable_count} livro(s) emprestado(s).')                       
        print(f'Há uma média de {copies_mean:.1f} cópia(s) por título.')
        space()

    # Imprime a lista de todos os livros    
    for individual_book in all_books:        
        print(individual_book)
        dash()
    
    space()
    space()