from dash import *
from error import *
from get_data import *
from fetch_data import *
#from devolution import *

def loan_book():
    user = ask_user_input()
    book = ask_book_input()

    def make_loan(user,book):
        
        # Verifica se o usuário já está com um livro emprestado
        for loaned_book in data['books']:
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

        save_data(data)

    make_loan(user,book)

loan_book()

'''    # Verifica se o usuário já está com um livro emprestado
        if 'borrowed_book' in user and user['borrowed_book'] != '':
            found_error('unavailable_user')
            print('Livro: ', user['borrowed_book'])
            print('Deseja realizar devolução?')
            print('1) SIM')
            print('2) NÃO, VOLTAR PARA O MENU')

            #make_devolution() #ISSO AQUI TÁ CERTO?
'''