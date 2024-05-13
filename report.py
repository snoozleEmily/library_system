from dash import *
from fetch_data import *

# Pega os dados do json
users = data.get('users', [])
books = data.get('books', [])

# 
individual_book = ''
all_books = []
individual_user = ''
all_users = []


for book in data['books']:
    book_id = book.get('ID', '')
    book_title = book.get('Título', '')
    book_author = book.get('Autor', '')
    book_year = book.get('Ano de Publicação', '')
    book_stock = book.get('Copias em Estoque', '')
    book_available = book.get('Copias Disponíveis', '')

    individual_book = f'//Livro: {book_title} - Autor(a): {book_author} - Ano de Publicação: {book_year} - Copias em Estoque: {book_stock} - Copias Disponíveis: {book_available}. '
    all_books.append(individual_book)


# Lista de todos os livros    
for individual_book in all_books:
    space()
    print(individual_book)
    dash()

'''
# Loop for users information
for user in data['users']:
    user_name = user.get('Nome', '')
    user_cpf = user.get('CPF', '')
    user_contact = user.get('Contato', '')
    user_book_title = user.get('Livro Em Posse', {}).get('Título', '')
    user_book_id = user.get('Livro Em Posse', {}).get('ID', '')

    individual_user = f'Nome: {user_name} - CPF: {user_cpf} - Contato: {user_contact} - Livro Em Posse: {user_book_title} (ID: {user_book_id})'
    all_users.append(individual_user)
'''

#Livros disponíveis
#Livros cadastrados

#Usuários cadastrados
#Relatório Geral