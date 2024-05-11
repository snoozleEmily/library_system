from error import *
from menu import *
from book import *
from user import *
from loan import * 
from devolution import *
from dash import *


while True:
    menu()
    button = input('Escolha uma opção: ')
    # o input não funciona pela primeira vez

    if button == '1':
        # Cria um novo livro
        create_book()
    elif button == '2':
        # Cria um novo usuário
        create_user()
    elif button == '3':
        # Faz empréstimo de um livro para algum usuário
        ask_user_input()
        ask_book_input()
    elif button == '4':
        # Faz devolução de algum livro emprestado
        make_devolution()
    elif button == '5':
        # Faz a consulta de um livro
        ask_book_input()
    elif button == '6':
        # Gera um relatório
        print('Relatório')
    elif button == '7':
        # Finaliza o programa
        print('Sessão Encerrada. Até mais!')
        break
    else:
        # Caso o input seja inválido retorna um erro e reinicia o loop para mostrar o menu 
        found_error('invalid_value')
        space()
        continue  
        