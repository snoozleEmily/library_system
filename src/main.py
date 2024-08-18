from dash import space
from menu import menu, reports_menu
from error import found_error
from book import create_book
from user import create_user
from loan import loan_book
from devolution import make_devolution
from get_book import ask_book_input
from report import books_report, users_report

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
            # Consulta um livro
            ask_book_input()
        case '6':
            reports_menu()
            report_type = input('Escolha uma opção: ')
            match report_type:
                case '1':
                    # Gera um relatório geral
                    users_report()
                    books_report()
                case '2':
                    # Gera um relatório de livros
                    books_report()
                case '3':
                    # Gera um relatório de usuários
                    users_report()                    
                case _:
                    found_error('invalid_value')
                    space()
                    continue
        case '7':
            # Finaliza o programa
            space()
            print('Sessão Encerrada. Até mais!')
            break
        case _:
            found_error('invalid_value')
            space()
            continue