from dash import *
from error import *
from get_data import *
from fetch_data import *
#from devolution import *

def loan_book():
    user, book = search_data()

    def make_loan(user,book):
        
        # Verifica se o usuário já está com um livro emprestado
        for lending_book in data['books']:
            if lending_book['Número de Identificação'] == book['Número de Identificação']:

                if lending_book['Copias Disponíveis'] == 0:
                    print("Livro indisponível no momento. Tente novamente mais tarde.")
                    return
                # Atualiza o número de copias disponíveis
                lending_book['Copias Disponíveis'] -= 1 
                break

        # Atualiza os dados usuário registrando o empréstimo
        user['borrowed_book'] = {
            'Título': book['Título'],
            'ID': book['Número de Identificação']
        }

        print("Emprestado:", book["Título"], "para", user["Nome"])
        print("Copias Disponíveis atualizadas:", lending_book['Copias Disponíveis'])

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