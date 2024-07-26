from dash import space
from menu import menu
from error import found_error
from book import create_book
from user import create_user
from loan import loan_book
from devolution import make_devolution
from get_book import ask_book_input
from report import all_books_report, all_users_report

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
            # Retorna erro se input é inválido e reinicia o loop
            found_error('invalid_value')
            space()
            continue