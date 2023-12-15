import requests
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    requisicao_dic = requisicao.json()
    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotacao_btc = requisicao_dic["BTCBRL"]["bid"]
    texto_resposta['text'] = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}
    '''
    print('requisicao_dic')


janela = Tk()
janela.title('Cotação de Moedas')
texto = Label(janela, text='Clique no botão para ver as cotações de moedas')
texto.grid(column=0, row=0)
botao = Button(janela, text='Buscar cotações', command=pegar_cotacoes)
botao.grid(column=0, row=1)
texto_resposta = Label(janela, text='')
texto_resposta.grid(column=0, row=2)

janela.mainloop()
