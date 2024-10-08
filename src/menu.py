from dash import *

def header() -> None:
    dash()
    print('Sistema de Gerenciamento Bibliotecário')
    dash()
    print('--> Menu')

def menu() -> None:
    header()
    print('1) Registrar Livro')
    print('2) Registrar Usuário')
    print('3) Registrar Locação')
    print('4) Registrar Devolução')
    print('5) Consultar Livro')
    print('6) Gerar Relatório')
    print('7) Sair')
    space()

def reports_menu() -> None:
    header()
    print('1) Gerar Relatório Geral')
    print('2) Gerar Relatório De Todos Os Livros')
    print('3) Gerar Relatório De Usuários Cadastrados')
    space()