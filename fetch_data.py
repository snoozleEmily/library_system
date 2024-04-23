import json
import os

#Pega os dados do storage
def fetch_storage_data():
    file_path = 'D:/Projects/Python-studies/ampli_university_snipets/library_system/storage.json' 
    
    if not os.path.exists(file_path): # Verifica se o arquivo existe
        raise FileNotFoundError(f"Arquivo '{file_path}' não encontrado.") # Caso não encontrado, lança uma exceção FileNotFoundError
    
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f: # Tenta abrir o arquivo e carregar os dados JSON
            return json.load(f)
        
    except json.decoder.JSONDecodeError as e:
        print("Erro ao decodificar JSON:", e) # Em caso de erro, ao decodificar o JSON, imprime o erro
        
        # Mostra o conteúdo do arquivo para ajudar na depuração do problema
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            print("Conteúdo do arquivo: ", f.read())
        raise

  
#Salva os livros novos no storage
def save_book_data(books_data):
    with open('D:/Projects/Python-studies/ampli_university_snipets/library_system/storage.json', 'w', encoding='utf-8-sig') as f:
        json.dump(books_data, f, ensure_ascii=False)

#Salva os usuários novos no storage
def save_user_data(users_data):
    with open('D:/Projects/Python-studies/ampli_university_snipets/library_system/storage.json', 'w', encoding='utf-8-sig') as f:
        json.dump(users_data, f, ensure_ascii=False)



#Atualiza mudanças de dados dos livros no storage
def update_data(data):
     with open('D:/Projects/Python-studies/ampli_university_snipets/library_system/storage.json', 'r+', encoding='utf-8-sig') as f:
        f.seek(0) #Ponteiro é defido para o início do arquivo
        json.dump(data, f, ensure_ascii=False)
        f.truncate() #Remove dados restantes após o update
        return data