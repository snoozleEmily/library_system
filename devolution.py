from dash import *
from error import *
from get_data import *
from fetch_data import *

def make_devolution():
    user = ask_user_input()
    book = user['Livro Em Posse']['ID']
    
    for loaned_book in data['books']:
        try:
            if loaned_book['ID'] == book:
                # Atualiza o número de copias disponíveis
                loaned_book['Copias Disponíveis'] += 1
                print('Livro: ')
                print(loaned_book)
                break
        # Ignora erro de chave ausente no dicionário
        except KeyError:
            pass
            
    # Atualiza o usuário    
    user['Livro Em Posse'] = ''

    space()
    print('Devolução feita com sucesso!')
    # Salva os novos dados
    save_data(data) 

make_devolution()
