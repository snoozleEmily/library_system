from dash import *
from menu import *
from book import *
from user import *
from loan import * 

while True:
    menu()
    button = input()
    
    if button == '1':
        create_book()
    elif button == '2':
        create_user()
    
    elif button == '3':
        loan()
        
    else:
        print('[ERRO] Opção inválida. Por favor, escolha uma das opções disponíveis no menu!')
        dash()

#Understanding classes and object-oriented programming - https://www.youtube.com/watch?v=_vr5faCXFo8