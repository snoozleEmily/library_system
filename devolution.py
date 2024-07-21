from dash import space
from get_user import ask_user_input
from fetch_data import pd, books_df, users_df, save_books, save_users

def make_devolution():    
    user: pd.Series = ask_user_input()
    book_id: str = user.loc['Livro Em Posse.ID']
    book_name: str = user.loc['Livro Em Posse.Título'] 
    
    for index, row in books_df.iterrows():   
        for title in row['Copias em Estoque']: 
            if title['ID'] == book_id and row['Título'] == book_name:
                
                title['Disponível'] = not title['Disponível']
                books_df.loc[index, 'Copias Disponíveis'] += 1                               
                    
                print('Livro: ')
                #print(books_df.loc[index])
                break 
    
    users_df.loc[['Livro Em Posse']] = {}
    #print(user_index)
    
    space()
    print('Devolução feita com sucesso!')
    
    #save_users(users_df)
    #save_books(books_df)   

    #del user, book_id, book_name
    
make_devolution()