from dash import dash, space
from error import found_error
from get_user import ask_user_input
from fetch_data import pd, books_df, users_df, save_books, save_users

def make_devolution() -> None:    
    books_df_copy = books_df.copy()
    users_df_copy = users_df.copy()    
    user = ask_user_input()
    
    book_id = user.loc['Livro Em Posse.ID']
    book_name = user.loc['Livro Em Posse.Título']     
    user_index = users_df_copy[users_df_copy['ID'] == user['ID']].index
    
    for index, row in books_df_copy.iterrows():   
        for title in row['Copias em Estoque']: 
            if title['ID'] == book_id and row['Título'] == book_name:
                title['Disponível'] = not title['Disponível']
                books_df_copy.loc[index, 'Copias Disponíveis'] += 1 
                print('Livro: ', row['Título'])
                break 
    
    space()
    print('Efetuar devolução?')
    print('1.SIM | 2.NÃO')
    correct_input = input() 

    match correct_input: 
        case '1':    
            # Remove valores antigos dos dataframes             
            users_df_copy.drop(user_index, inplace=True)  
            
            # Atualiza o DataFrame de usuarios
            user['Livro Em Posse.Título'] = None
            user['Livro Em Posse.ID'] = None    
            users_df_copy = pd.concat([users_df_copy, pd.DataFrame([user])], ignore_index=True)   
            
            space()
            print('Devolução feita com sucesso!')
            print('Emprestado:', book_name, 'para', user['Nome'])
            print('Copias Disponíveis atualizadas:',  books_df_copy.at[index, 'Copias Disponíveis'])
            dash()
            
            save_users(users_df_copy)
            save_books(books_df_copy)           
        case '2':
            pass 
        case _:
            found_error('invalid_value')
    
if __name__ == '__main__':    
    make_devolution()