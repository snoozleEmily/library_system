from typing import Union, Callable

from dash import space
from fetch_data import pd, users_df, save_users
from error import found_error

# Declarando variável global
_single_user: dict = {}

#Cadastro de Usuários: nome, número de identificação (CPF) e contato 
class User:
    def __init__(self, name, cpf, info):
        self.name = name
        self.cpf = cpf
        self.info = info

def create_user() -> Union[dict, Callable[[pd.DataFrame], pd.DataFrame]]:
    input_prompts = [
        ('Nome completo do usuário', 'name'),
        ('CPF', 'cpf'),
        ('Número de telefone', 'info')
    ]
    
    # Garante que os inputs estão corretos
    for prompt, attribute in input_prompts:
        while True:
            user_input = input(f'{prompt}: ')
            error = 'invalid_value' # Determina erro padrão

            def number_verify():
                # Levanta um erro caso o input não seja numérico
                if not user_input.isdigit():
                    raise ValueError
            try:
                match attribute:
                    case 'name':
                        if user_input == '' or user_input.isdigit():
                            # Levanta um erro caso o input seja uma string vazia ou contenha apenas dígitos
                            error = 'number_length'
                            raise ValueError
                        name = user_input

                    case 'cpf':
                        number_verify()
                        if len(user_input) != 11:
                            # Levanta um erro caso o input não contenha 11 dígitos
                            error = 'cpf_length'
                            raise ValueError
                        cpf = user_input

                    case 'info':
                        number_verify()
                        if len(user_input) != 9:
                            # Levanta um erro caso o input não contenha 9 dígitos
                            error = 'info_length'
                            raise ValueError
                        info = user_input
                break
            
            except ValueError:
                found_error(error)

    # Passando as informações da classe User para uma variável
    new_user = User(name, cpf, info)

    global _single_user
    _single_user = {
            'ID': len(users_df) + 1,
            'Nome': new_user.name,
            'CPF': new_user.cpf,
            'Contato': new_user.info,
            'Livro Em Posse': {}
            }
    
    return _single_user and add_new_user(users_df)

def add_new_user(users_df: pd.DataFrame) -> pd.DataFrame:
    new_user_df = pd.DataFrame([_single_user])

    space()
    print('Adicionar PERMANETEMENTE os seguintes dados?')
    print(_single_user)
    print('1.SIM | 2.NÃO')
    correct_input = input()   

    match correct_input:             
        case '1': 
            # Salva os dados do novo usuário 
            updated_users_df = pd.concat([users_df, new_user_df], ignore_index=True) 
            save_users(updated_users_df)
            print('Usuário Registrado Com Sucesso!')        
        case '2':        
            print('1) Menu principal')
            print('2) Inserir dados novamente')
            
            redo_input = input()
            match redo_input:
                case '1':
                    _single_user.clear()
                    pass
                case '2': 
                    create_user()
        case _:
            found_error('invalid_value')
            correct_input = input('1.SIM | 2.NÃO')

    _single_user.clear()
    return users_df

if __name__ == '__main__':
    create_user()