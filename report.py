from dash import dash, space
from fetch_data import pd, books_df, users_df

# Variáveis para armazenar informações de um único livro/usuário
individual_book = ''
individual_user = ''

# Listas para armazenar informações de todos os livros/usuários
all_books = []
all_users = []

def books_report() -> None:
    unavailable_count = 0  # Contador de livros indisponíveis (emprestados)
    number_of_titles = len(books_df)  #Título seria o nome, e.g. Orgulho e Preconceito
    sum_all_copies = 0  #e.g. Cópias/Exemplares = lista com ID e dispónibilidade (booleano) 
    
    # Percorre todos os livros de books.json
    for _, book in books_df.iterrows():
        book_title = book['Título']
        book_author = book['Autor']
        book_year = book['Ano de Publicação']
        book_stock = book['Copias em Estoque']
        book_available = book['Copias Disponíveis']
        
        copies_stock = len(book_stock)   
        unavailable_count += sum(1 for copy in book_stock if not copy['Disponível'])           

        # Formata as informações de cada livro e o adiciona à lista de todos os livros
        individual_book = f'//Livro: {book_title} | Autor(a): {book_author} | Ano De Publicação: {book_year\
            } | Copias Em Estoque: {copies_stock} | Copias Disponíveis Para Empréstimo: {book_available} '
        all_books.append(individual_book)    

        # Conta a quantidade de livros em estoque        
        sum_all_copies += copies_stock 
    
    # Imprime a quantidade total de livros em estoque
    space()
    dash()  
    print('RELATÓRIO LIVROS')
    dash()
    print(f'Há um total de {number_of_titles} títulos e {sum_all_copies} exemplares em estoque')
    space()
    
    # Imprime a quantidade de livros emprestados e a média de cópias por título
    if unavailable_count != 0:
        copies_mean = sum_all_copies/number_of_titles 
        print(f'Há {unavailable_count} cópia(s) emprestada(s).')                       
        print(f'Há uma média de {copies_mean:.1f} cópia(s) por título.')
        space()

    # Imprime a lista de todos os livros    
    for individual_book in all_books:  
        dash()      
        print(individual_book)
        
    dash()
    space()
    space()
    all_books.clear()
    
def users_report() -> None:
    for _, user in users_df.iterrows():
        user_name = user['Nome']
        user_id = user['CPF']
        user_info = user['Contato']
        user_loan = user['Livro Em Posse.Título']        
        
        # Formata as informações de cada usuário e o adiciona à lista de todos os usuários
        loan_checker = f'Nenhum' if pd.isna(user_loan) or not user_loan else user_loan
        individual_user = f'//Nome: {user_name} | CPF: {user_id} | Contato: {user_info} | Livro Em Posse: {loan_checker} '
        all_users.append(individual_user)

    space()
    dash()    
    print('RELATÓRIO USUÁRIOS')
    dash()
    print(f'Há um total de {len(all_users)} usuário(s) cadastrado(s).')
    space()
    
    # Imprime a lista de todos os usuários    
    for individual_user in all_users:
        dash()
        print(individual_user)
        
    dash()    
    space()
    space()
    all_users.clear()

if __name__ == '__main__':
    books_report()
    users_report()    