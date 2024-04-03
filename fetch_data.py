import json

#Pegar os dados do storage
def fetch_storage_data():
    with open('D:/Projects/Python-studies/Ampli University Snipets/library_system/storage.json', 'r') as f:
        return json.load(f)

#Salvar os livros novos no storage
def save_book_data(books_data):
    with open('D:/Projects/Python-studies/Ampli University Snipets/library_system/storage.json', 'w', encoding='utf-8') as f:
        json.dump(books_data, f, ensure_ascii=False)

#Salvar os usuários novos no storage
def save_user_data(users_data):
    with open('D:/Projects/Python-studies/Ampli University Snipets/library_system/storage.json', 'w', encoding='utf-8') as f:
        json.dump(users_data, f, ensure_ascii=False)