from dash import dash
from error import found_error
from get_user import ask_user_input
from get_book import ask_book_input
from fetch_data import pd,books_df, users_df,save_books, save_users

def loan_book():
    books_df_copy = books_df.copy()
    users_df_copy = users_df.copy()    

    user = ask_user_input() # OS USERS ESTÃO SENDO SALVOS LOGO QUANDO RODO O CODIGO????????
    book = ask_book_input()

    available_id = None
    for copy in book['Copias em Estoque']: #TypeError: 'NoneType' object is not subscriptable?????????
        if copy['Disponível']:              # Sometimes I get this err, wtf? At other times this shit works
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
    
    # Remove usuário selecionado do dataframe
    user_index = users_df_copy[users_df_copy['ID'] == user['ID']].index
    users_df_copy.drop(user_index, inplace=True)
    
    # Adiciona o usuário com o livro emprestado
    user['Livro Em Posse.Título'] = book['Título']
    user['Livro Em Posse.ID'] = available_id
    users_df_copy = pd.concat([users_df_copy, pd.DataFrame([user])], ignore_index=True)
    print(user)
    
    dash()
    print('Emprestado:', book['Título'], 'para', user['Nome'])
    print('Copias Disponíveis atualizadas:',  books_df_copy.at[index, 'Copias Disponíveis'])
    dash()

    save_books(books_df_copy)
    save_users(users_df_copy)

if __name__ == '__main__':
    loan_book()