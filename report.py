from dash import *
#from error import *
from fetch_data import *

# Extract necessary information
users = data.get('users', [])
books = data.get('books', [])
# Declares variables
book_text = ''
books_info = []
user_text = ''
users_info = []

for book in data['books']:
    book_id = book.get('ID', '')
    book_title = book.get('Título', '')
    book_author = book.get('Autor', '')
    book_year = book.get('Ano de Publicação', '')
    book_stock = book.get('Copias em Estoque', '')
    book_available = book.get('Copias Disponíveis', '')

    book_text = f'//Livro: {book_title} - Autor(a): {book_author} - Ano de Publicação: {book_year} - Copias em Estoque: {book_stock} - Copias Disponíveis: {book_available}. '
    books_info.append(book_text)


# Loop for users information
for user in data['users']:
    user_name = user.get('Nome', '')
    user_cpf = user.get('CPF', '')
    user_contact = user.get('Contato', '')
    #user_book_title = user.get('Livro Em Posse', {}).get('Título', '')
    #user_book_id = user.get('Livro Em Posse', {}).get('ID', '')

    user_text = f'Nome: {user_name} - CPF: {user_cpf} - Contato: {user_contact} ' # - Livro Em Posse: {user_book_title} (ID: {user_book_id})'
    users_info.append(user_text)



# Lista de todos os livros    
for book_text in books_info:
    space()
    print(book_text)
    dash()


#Livros disponíveis
#Livros cadastrados

#Usuários


# Format data into text


# Print or save the text

