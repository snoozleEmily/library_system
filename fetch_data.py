import json
import pandas as pd
import pandas as pd

books_path = 'D:/Projects/Python-studies/ampli_university_snipets/library_system/books.json'
users_path = 'D:/Projects/Python-studies/ampli_university_snipets/library_system/users.json'

def fetch_books() -> dict:
    with open(books_path, 'r', encoding='utf-8-sig') as f: 
        return json.load(f)
    
def fetch_users() -> dict:
    with open(users_path, 'r', encoding='utf-8-sig') as f: 
        return json.load(f)

all_books_data = fetch_books() 
all_users_data = fetch_users()

books_df: pd.DataFrame = pd.json_normalize(all_books_data)
users_df: pd.DataFrame = pd.json_normalize(all_users_data)

def save_books(new_book) -> None:
    new_book: dict = new_book.to_dict(orient='records')
    with open(books_path, 'w', encoding='utf-8-sig') as f:
        json.dump(new_book, f, ensure_ascii=False)

def save_users(new_user) -> None:    
    for index in range(len(new_user)):
        loaned_book = new_user.iloc[index][['Livro Em Posse.Título', 'Livro Em Posse.ID']]
        print(loaned_book.isna().any())
        
        if loaned_book.isna().any(): loaned_book = {}
        else: loaned_book = {
            'Título': loaned_book['Livro Em Posse.Título'],
            'ID': loaned_book['Livro Em Posse.ID']
        }     
    print(new_user)
    new_user: dict = new_user.to_dict(orient='records')    
    #with open(users_path, 'w', encoding='utf-8-sig') as f:
    #    json.dump(new_user, f, ensure_ascii=False)

save_users(users_df)