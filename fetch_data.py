import json
file_path = 'D:/Projects/Python-studies/ampli_university_snipets/library_system/storage.json'

#Pega os dados do storage
def fetch_storage_data():
    with open(file_path, 'r', encoding='utf-8-sig') as f: 
        return json.load(f)

data = fetch_storage_data() #Variável para referenciar a função

#Atualiza os dados no storage    
def save_data(new_data):
    with open(file_path, 'w', encoding='utf-8-sig') as f:
        json.dump(new_data, f, ensure_ascii=False)