from error import found_error
from get_user import ask_user_input
from get_book import ask_book_input
from fetch_data import books_df, users_df,save_books, save_users

def loan_book():
    user = ask_user_input()
    book_df = ask_book_input()
    book = books_df.squeeze()
            
    # Verifica se o usuário já está com um livro emprestado
    for index, loaned_book in books_df.iterrows():
        if loaned_book['ID'] == book['ID']:
            if loaned_book['Copias Disponíveis'] == 0:
                found_error('unavailable_book')
                return
            # Atualiza o número de copias disponíveis
            loaned_book['Copias Disponíveis'] -= 1 
            break

    # Atualiza os dados usuário registrando o empréstimo
    user['Livro Em Posse.Título'] = book['Título']
    user['Livro Em Posse.ID'] = book['ID']
        

    print("Emprestado:", book["Título"], "para", user["Nome"])
    print("Copias Disponíveis atualizadas:", loaned_book['Copias Disponíveis'])

    save_books(books_df)
    save_users(users_df)

if __name__ == '__main__':
    loan_book()