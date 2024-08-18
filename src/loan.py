from dash import dash, space
from error import found_error
from get_user import ask_user_input
from get_book import ask_book_input 
from fetch_data import pd, books_df, users_df, save_books, save_users

def loan_book() -> None:
    books_df_copy = books_df.copy()
    users_df_copy = users_df.copy()
    user = ask_user_input() 
        
    if not pd.isna(user.get('Livro Em Posse.Título')):
        found_error('unavailable_user') 
        return
    else: 
        available_id = None 
        book = ask_book_input(year_applicable=False)
        user_index = users_df_copy[users_df_copy['ID'] == user['ID']].index
        book_index = books_df_copy[books_df_copy['Título'] == book['Título']].index[0]        
        available_copies = books_df_copy.at[book_index, 'Copias Disponíveis']
        copies_in_stock = books_df_copy.at[book_index, 'Copias em Estoque'] 
        
        # Obtem a ID do livro selecionado
        for copy in book['Copias em Estoque']:
            if copy['Disponível']:              
                available_id = copy['ID']
                break                   
        
        # Verifica se o livro está disponível        
        if available_copies == 0:
            found_error('unavailable_book')
            return
            
        # Atualiza o número de copias disponíveis           
        for copy in copies_in_stock:
            if copy['ID'] == available_id:
                available_copies -= 1 
                copy['Disponível'] = False
                break        
        
        space()
        print('Efetuar empréstimo?')
        print('1.SIM | 2.NÃO')
        correct_input = input() 

        match correct_input: 
            case '1':
                # Remove valores antigos dos dataframes             
                users_df_copy.drop(user_index, inplace=True) 
                books_df_copy.drop(book_index, inplace=True)                    
                
                # Atualiza os valores
                user['Livro Em Posse.Título'] = book['Título']
                user['Livro Em Posse.ID'] = available_id
                users_df_copy = pd.concat([users_df_copy, pd.DataFrame([user])], ignore_index=True)
                
                book['Copias Disponíveis'] = available_copies
                books_df_copy = pd.concat([books_df_copy, pd.DataFrame([book])], ignore_index=True)
                        
                dash()
                print('Empréstimo feito com sucesso!')
                print('Emprestado:', book['Título'], 'para', user['Nome'])
                print('Copias Disponíveis atualizadas:',  books_df_copy.at[book_index, 'Copias Disponíveis'])
                dash()
                
                save_books(books_df_copy)
                save_users(users_df_copy)
            case '2':
                pass
            case _:
                found_error('invalid_value')

if __name__ == '__main__':
    loan_book()