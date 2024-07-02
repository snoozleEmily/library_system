from dash import *
from menu import *
from error import *
from book import *
from user import *
from loan import * 
from devolution import *
from report import *

while True:
    menu()
    choice = input('Escolha uma opção: ')
    match choice:
        case '1':
            # Cria um novo livro
            create_book()
        case '2':
            # Cria um novo usuário
            create_user()
        case '3':
            # Faz empréstimo de um livro para algum usuário
            loan_book()
        case '4':
            # Faz devolução de algum livro emprestado
            make_devolution()
        case '5':
            # Faz a consulta de um livro
            ask_book_input()
        case '6':
            # Gera um relatório
            all_users_report()
            all_books_report()
        case '7':
            # Finaliza o programa
            print('Sessão Encerrada. Até mais!')
            break
        case _:
            # Se input inválido retorna um erro e reinicia o loop
            found_error('invalid_value')
            space()
            continue