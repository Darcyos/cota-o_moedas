import requests
from tkinter import *

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
requisicao_dic = requisicao.json()

janela = Tk()
janela.geometry('250x300')
janela.title("Cotação Atual de Moedas")

def dolar():
    cotacao_dolar = float(requisicao_dic['USDBRL']['bid'])
    texto_resposta['text'] = f'Dólar: {cotacao_dolar: .2f}'

def euro():
    cotacao_euro = float(requisicao_dic['EURBRL']['bid'])
    texto_resposta['text'] = f'Euro: {cotacao_euro: .2f}'

def bitcoin():
    cotacao_btc = float(requisicao_dic['BTCBRL']['bid'])
    texto_resposta['text'] = f'Bitcoin: {cotacao_btc: .2f}'

texto = Label(janela, text="Clique no botão para ver a cotação desejada")
texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Dolar", command=dolar)
botao.grid(padx=10, pady=10)

botao = Button(janela, text="Euro", command=euro)
botao.grid(padx=10, pady=10)

botao = Button(janela, text="Bitcoin", command=bitcoin)
botao.grid(padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=5, padx=10, pady=10)



janela.mainloop()