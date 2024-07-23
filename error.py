import datetime
from dash import space

def get_current_year() -> int:
    return datetime.datetime.now().year 

error_messages = {
    # Erros de Entrada 
    'cpf_length': '[ERRO] Ha, ha! Parece que esse CPF não tem 11 dígitos. Não deixe nenhum para trás!',
    'info_length': '[ERRO] Oh là là! Não sabia que existia algum número de telefone assim. Por favor digite exatamente 9 números.',
    'year_length': '[ERRO] O ano precisa ter quatro números. Nossa biblioteca não aceita livros de tal século!',
    'year_current': lambda: f'[ERRO] Ano inválido. Parece que estamos viajando para o futuro! Por favor, insira um ano válido ANTES de {get_current_year()}.',
    'exceeded_book_limit': '[ERRO] O número de cópias disponíveis não pode ser maior do que o das cópias em estoque.',

    # Valores Inválidos
    'invalid_value': '[ERRO] Essa não! Esse valor parece ser inválido. Por favor, tente novamente.',
    'invalid_CPF': '[ERRO] Oops! Não conseguimos encontrar nenhum usuário com este CPF. Será que os números estão corretos?',
    'invalid_name': '[ERRO] Hum... Parece que não tem ninguém com esse nome por aqui. Será que você que digitou certinho?',
    'invalid_book': '[ERRO] Parece que esse livro não está em nossa biblioteca. Será que você digitou certinho?',
    
    # Itens Indisponíveis
    'unavailable_book': '[ERRO] Parece que outra pessoa já pegou este livro emprestado. Faça uma pausa, pegue um café e tente novamente amanhã. Quem sabe esse livro não estará disponível na próxima vez!',
    'unavailable_user': '[ERRO] Uh-oh! Parece que temos um devorador de livros por aqui! Esse usuário já possui um livro emprestado. Faça a devolução do mesmo antes de cadastrar outro empréstimo.',
    'missing_user': '[ERRO] Parece que algum dos exemplares já foi emprestado, porém olhei em todos os cantos e não encontrei nenhum usuário registrado com esse livro. Por favor, registre-o agora para evitar problemas.'

}

def found_error(entry_type):
    print(error_messages[entry_type])
