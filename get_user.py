from typing import Optional

from dash import space
from fetch_data import pd, users_df
from error import found_error

def get_user_data(attribute: str) -> Optional[pd.Series]:
        search_value = input(f"Digite o {attribute}: ")
        error_type = 'value' # Define erro padrão
        
        if attribute == 'Nome': error_type = 'name'
        elif attribute == 'CPF':
            # CPF deve ter 11 digitos
            try: 
                if len(search_value) != 11 and search_value.isdigit():                    
                    found_error('cpf_length')
                else:
                    error_type = 'CPF'
            except ValueError:
                found_error(error_type)
                ask_user_input()
                return
        else:
            found_error(f'invalid_{error_type}')
            ask_user_input()

        for index, row in users_df.iterrows():
            if row[attribute] == search_value:
                print('Usuário encontrado: ')
                print(row)
                space()
                return row
            
         # Caso o usuário não for encontrado, exibe um erro  
        found_error(f'invalid_{error_type}')
        ask_user_input()
    
def ask_user_input() -> Optional[pd.Series]:
        print('Pesquisar usuário por: ')
        space()
        print('1) Nome')
        print('2) CPF')

        user_search = input('') 
        match user_search:
            case '1':
                reader = get_user_data('Nome')
                return reader
            case '2':
                reader = get_user_data('CPF')
                return reader
            case _:
                found_error('invalid_value') 
                ask_user_input()
