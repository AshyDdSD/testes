import sqlite3
from PySimpleGUI import PySimpleGUI as sg

# Design da tela
sg.theme('Dark Grey 13')
tela = [
    [sg.Text('Email: '), sg.Input(size=(30, 0), key='email')],
    [sg.Text('Senha: '), sg.Input(size=(30, 0), key='senha')],
    [sg.Button('Entrar')]
]

# Inicialização da tela
janela = sg.Window('login').layout(tela)
button, values = janela.read()

# Recolhendo dados da interface
email = values['email']
senha = values['senha']
print(email, senha)

# Banco de Dados
db = sqlite3.connect('Teste.db')
cursor = db.cursor()

# cursor.execute
cursor.execute(f"INSERT INTO login (Email, Senha) VALUES('{email}', '{senha}')")
db.commit()
db.close()