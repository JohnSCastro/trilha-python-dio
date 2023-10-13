import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import datetime as dt

cotacao_periodo = "https://economia.awesomeapi.com.br/json/daily/USD-BRL"

tempo = int(input("Qual periodo em dias você quer saber a cotação do Dolar?")
lista = []
data = []
hoje = dt.date.today()
dia = hoje.day
mes = hoje.month
def get_periodo ():
    response = requests.get(f'{cotacao_periodo}/{tempo}')            
    return response.json() if response.status_code == 200 else None 

valor_periodo = get_periodo()

for i in range(tempo):
    lista.append(valor_periodo[i]['bid'])


for i in range(tempo):
    if (dia-i) < 0 and (mes == 1 or mes == 2 or mes == 4 or mes == 6 or mes == 8 or mes == 9 or mes == 11):
        dia = 31
        data.append(f'{dia}')
        dia = dia - 1
    elif (dia-i) < 0 and (mes == 5 or mes == 7 or mes == 10 or mes == 12):
        dia = 30
        data.append(f'{dia}')
        dia = dia - 1
    elif (dia-i) < 0 and mes == 3:
        dia = 28
        data.append(f'{dia}')
        dia = dia - 1
    else:
        data.append(f'{dia}')
        dia = dia - 1


data = data[::-1]
lista = lista[::-1]
print(data)
print(lista)
plt.plot(data, lista)
plt.show()



