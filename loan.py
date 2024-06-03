from dash import *
from error import *
from get_data import *
from fetch_data import *

def loan_book():
    user = ask_user_input()
    book = ask_book_input()

    def make_loan(user,book):        
        # Verifica se o usuário já está com um livro emprestado
        for loaned_book in all_books_and_users_data['books']:
            if loaned_book['Número de Identificação'] == book['Número de Identificação']:
                if loaned_book['Copias Disponíveis'] == 0:
                    found_error('unavailable_book')
                    return
                # Atualiza o número de copias disponíveis
                loaned_book['Copias Disponíveis'] -= 1 
                break

        # Atualiza os dados usuário registrando o empréstimo
        user['Livro Em Posse'] = {
            'Título': book['Título'],
            'ID': book['Número de Identificação']
        }

        print("Emprestado:", book["Título"], "para", user["Nome"])
        print("Copias Disponíveis atualizadas:", loaned_book['Copias Disponíveis'])

        save_data(all_books_and_users_data)

    make_loan(user,book)