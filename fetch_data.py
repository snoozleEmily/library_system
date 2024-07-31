import json
import pandas as pd

users_path = r'Python-studies\ampli_university_snipets\library_system\users.json'
books_path = r'Python-studies\ampli_university_snipets\library_system\books.json'

def fetch_books() -> dict:
    with open(books_path, 'r', encoding='utf-8-sig') as f: 
        return json.load(f)
    
def fetch_users() -> dict:
    with open(users_path, 'r', encoding='utf-8-sig') as f: 
        return json.load(f)

all_books = fetch_books() 
all_users = fetch_users()

books_df: pd.DataFrame = pd.json_normalize(all_books)
users_df: pd.DataFrame = pd.json_normalize(all_users)

def save_books(new_book) -> None:
    new_book: dict = new_book.to_dict(orient='records')
    with open(books_path, 'w', encoding='utf-8-sig') as f:
        json.dump(new_book, f, ensure_ascii=False)

def save_users(new_user) -> None:       
    new_user: dict = new_user.to_dict(orient='records') 
    
    for index in range(len(new_user)):
        user = new_user[index]
        loaned_book_title = user.get('Livro Em Posse.Título')
        loaned_book_id = user.get('Livro Em Posse.ID')        
        
        # Remove valores antigos
        user.pop('Livro Em Posse.Título', None) 
        user.pop('Livro Em Posse.ID', None)  
        
        # Caso nenhum livro esteja em posse, cria um dicionário vazio
        # para que não tenham valores NaN 
        if  pd.isna(loaned_book_title) or pd.isna(loaned_book_id):            
            loaned_book = {}            
        else: loaned_book = {
            'Título': loaned_book_title,
            'ID': loaned_book_id
        }        
        user['Livro Em Posse']  = loaned_book 
        
    with open(users_path, 'w', encoding='utf-8-sig') as f:
        json.dump(new_user, f, ensure_ascii=False)

if __name__ == '__main__':
    fetch_books()
    fetch_users()    
    save_books(books_df)
    save_users(users_df)