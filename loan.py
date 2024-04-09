from fetch_data import *

data = fetch_storage_data()
new_data = update_data(data)

class Loan():
    def __init__(self, book, book_id, user, user_id):
        self.book = book
        self.id = id
        self.book_id = book_id
        self.user = user
        self.user_id = user_id
    
def loan_book():
    print('Pesquisar livro por: ')
    print('1) Nome')
    print('2) Autor')
    print('3) Ano de Publicação')
    print('4) Livros Disponíveis')
    print('5) ID')
    search_type = input('')

    if search_type not in ['1', '2', '3', '4', '5']:
        print(['ERRO'])
        
    elif search_type == '1':
        print('you chose 1')

    elif search_type == '2':
        print('you chose 2')

    elif search_type == '3':
        print('you chose 3')

    elif search_type == '4':
        print('you chose 4')

    elif search_type == '5':
        print('you chose 5')

loan_book()