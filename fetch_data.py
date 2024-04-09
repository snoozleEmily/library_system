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

#Atualizar mudanças de dados dos livros no storage
def update_data(data):
     with open('D:/Projects/Python-studies/Ampli University Snipets/library_system/storage.json', 'r+', encoding='utf-8-sig') as f:
        f.seek(0)
        json.dump(data, f, ensure_ascii=False)
        f.truncate()
        return data