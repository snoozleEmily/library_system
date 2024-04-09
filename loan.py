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

print(new_data)