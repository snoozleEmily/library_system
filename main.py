from error import *
from menu import *
from book import *
from user import *
from loan import * 
from dash import *


while True:
    menu()
    button = input('Escolha uma opção: ')
    # o input não funciona pela primeira vez

    if button == '1':
        create_book()

    elif button == '2':
        create_user()
    
    elif button == '3':
        loan_book()
    
    else:
        found_error('invalid_value')
        space()
        continue  # Restart the loop to display the menu again
        