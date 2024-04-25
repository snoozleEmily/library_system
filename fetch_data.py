import json

#Pega os dados do storage
def fetch_storage_data():
    file_path = 'D:/Projects/Python-studies/ampli_university_snipets/library_system/storage.json' 
    with open(file_path, 'r', encoding='utf-8-sig') as f: 
        return json.load(f)
        
#Salva os livros novos no storage
def save_book_data(books_data):
    with open('D:/Projects/Python-studies/ampli_university_snipets/library_system/storage.json', 'w', encoding='utf-8-sig') as f:
        json.dump(books_data, f, ensure_ascii=False)

#Salva os usuários novos no storage
def save_user_data(users_data):
    with open('D:/Projects/Python-studies/ampli_university_snipets/library_system/storage.json', 'w', encoding='utf-8-sig') as f:
        json.dump(users_data, f, ensure_ascii=False)