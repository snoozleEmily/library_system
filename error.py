from dash import *
import datetime

current_year = datetime.datetime.now().year # Obter o ano atual
#length  9 for phone and 11 for cpf

error_messages = {
    'return_menu': '[ERRO] Ixi... Me perdi aqui. Vamos precisar voltar para o menu.',

    # Erros de Entrada 
    'number_length': '',
    'year_length': '[ERRO] O ano precisa ter quatro números. Nossa biblioteca não aceita livros tão antigos assim!',
    'year_current': f'[ERRO] Ano inválido. Parece que estamos viajando para o futuro! Por favor, insira um ano válido ANTES de {current_year}.',
    'exceeded_book': '[ERRO] O número de cópias emprestadas não pode ser maior do que o das cópias em estoque.',

    # Valores Inválidos
    'invalid_value': '[ERRO] Essa não! Esse valor parece ser inválido. Por favor, tente novamente.',
    'invalid_CPF': '[ERRO] Oops! Não conseguimos encontrar nenhum usuário com este CPF. Será que os números estão corretos?',
    'invalid_name': '[ERRO] Hum... Parece que não tem ninguém com esse nome por aqui. Será que você que digitou certinho?',
    'invalid_book': '[ERRO] Parece que esse livro não está em nossa biblioteca. Será que você digitou certinho?',
    
    # Itens Indisponíveis
    'unavailable_book': '[ERRO] Parece que outra pessoa já pegou este livro emprestado. Faça uma pausa, pegue um café e tente novamente amanhã. Quem sabe esse livro não decide esperar por você na prateleira da próxima vez!',
    'unavailable_user': '[ERRO] Uh-oh! Parece que temos um devorador de livros por aqui! Esse usuário já possui um livro emprestado. Faça a devolução do mesmo antes de cadastrar outro empréstimo.'
}

def found_error(entry_type):
    if entry_type in error_messages:
        print(error_messages[entry_type])
        space()

