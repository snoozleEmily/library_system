from dash import *
# Será que passo todos os erros nesse módulo?
error_messages = {
    'CPF_value': '[ERRO] Oops! Não conseguimos encontrar nenhum usuário com este CPF. Será que os números estão corretos?',
    'name_value': '[ERRO] Hum... Parece que não tem ninguém com esse nome por aqui. Você tem certeza que digitou corretamente?',
    'any_book_value': '[ERRO] Parece que esse livro não está em nossa biblioteca. Ou você digitou errado ou ele decidiu fazer uma viagem em outras bibliotecas.',
    'invalid_value': '[ERRO] Essa não! Esse valor parece ser inválido. Por favor, tente novamente.'
}

def not_found_error(entry_type):
    space()
    if entry_type in error_messages:
        print(error_messages[entry_type])

#not_found_error('name_value')




