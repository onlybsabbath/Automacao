# Importando as Bibliotecas
import pyautogui
import time
import pandas as pd

# Passo 1: Entrar no site da empresa
pyautogui.PAUSE = 0.9

pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# Passo 2: Fazer login
time.sleep(5)

pyautogui.click(x=455, y=365)

pyautogui.write('seuemail@gmail.com')
pyautogui.press('tab')
pyautogui.write('minha_Senha')
pyautogui.press('tab')
pyautogui.press('enter')

# Passo 3: Importar a base de dados
tabela = pd.read_csv('produtos.csv')

# Passo 4: Cadastrar os produtos
time.sleep(5)

for linha in tabela.index:
    pyautogui.click(x=545, y=244)

    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter')

    pyautogui.scroll(10000)