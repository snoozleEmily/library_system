from dash import *
from fetch_data import *

# Comentário bom
individual_book = ''
all_books = []

individual_user = ''
all_users = []

def all_books_report():
    for book in data['books']:
        book_title = book['Título']
        book_author = book['Autor']
        book_year = book['Ano de Publicação']
        book_stock = book['Copias em Estoque']
        book_available = book['Copias Disponíveis']
        
        # Conta o número de cópias em estoque
        copies_stock = 0
        for _ in book_stock: 
          copies_stock += 1   

        individual_book = f'//Livro: {book_title} | Autor(a): {book_author} | Ano De Publicação: {book_year} | Copias Em Estoque: {copies_stock} | Copias Disponíveis Para Empréstimo: {book_available} '
        all_books.append(individual_book)

        # Lista de todos os livros    
        for individual_book in all_books:
            dash()
            print(individual_book)
            dash()

def all_users_report():
    for user in data['users']:
        user_name = user['Nome']
        user_id = user['CPF']
        user_info = user['Contato']
        user_loan = user['Livro Em Posse']        

        individual_user = f'//Nome: {user_name} | CPF: {user_id} | Contato: {user_info} | Livro Em Posse: {user_loan} '
        all_users.append(individual_user)

        # Lista de todos os livros    
        for individual_user in all_users:
            dash()
            print(individual_user)
            dash()

#Livros disponíveis
#def available_books_report():
#    pass

#Livros cadastrados
#def stock_books_report():
#    pass

#Relatório Geral
def generate_general_report():
    all_books_report()
    all_users_report()
    # Os valores se repetem?


generate_general_report()