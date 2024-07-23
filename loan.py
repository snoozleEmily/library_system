from dash import dash
from error import found_error
from get_user import ask_user_input
from get_book import ask_book_input
from fetch_data import books_df, users_df, save_books, save_users

def loan_book():
    books_df_copy = books_df.copy()
    users_df_copy = users_df.copy()    

    user = ask_user_input()
    title_df = ask_book_input()
    book = title_df.squeeze()

    available_id = None
    for copy in book['Copias em Estoque']:
        if copy['Disponível']:
            available_id = copy['ID']
            break
            
    # Verifica se o usuário já está com um livro emprestado
    for index, row in books_df_copy.iterrows():
        copies_in_stock = books_df_copy.at[index, 'Copias em Estoque']
        '''
        DOES NOT WORK
        if row['Copias Disponíveis'] == 0:
            found_error('unavailable_book')
            return
        '''
        
        for copy in copies_in_stock:   
            if copy['ID'] == available_id:  
                # Atualiza o número de copias disponíveis
                books_df_copy.at[index, 'Copias Disponíveis'] -= 1 
                copy['Disponível'] = False
                break

    # Atualiza os dados usuário registrando o empréstimo
    for index, row in users_df_copy.iterrows():
        if user['ID'] == row['ID']:
            user['Livro Em Posse'] = {
                    'Título': book['Título'],
                    'ID': available_id
                    }

    dash()
    print('Emprestado:', book['Título'], 'para', user['Nome'])
    print('Copias Disponíveis atualizadas:',  books_df_copy.at[index, 'Copias Disponíveis'])
    dash()

    save_books(books_df_copy)
    save_users(users_df_copy)

if __name__ == '__main__':
    loan_book()