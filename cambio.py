
import requests
import json
import pandas as pd
import decimal



url = "http://data.fixer.io/api/latest?access_key=3fbfd1fd46eb28d638ba12e895ce1bef"
print("Acessando Base de Dados...")
response = requests.get(url)
if response.status_code==200:
	print("Conseguiu acessar base de dados!")
	print("Buscando informações das moedas...")
	print(response)
	dados = response.json()
	day = dados["date"]
	print("Acessando dados do dia %s/%s/%s" % (day[8:],day[5:7],day[0:4]))
	print(dados['rates']['EUR'])
	print(dados['rates']['BRL'])
	print(dados['rates']['USD'])
	print(dados['rates']['BTC'])
	

	euro_real = round(dados['rates']['BRL'] / dados['rates']['EUR'], 2)
	dolar_real = round(dados['rates']['BRL'] / dados['rates']['USD'], 2)
	btc_real = round(dados['rates']['BRL'] / dados['rates']['BTC'], 2)


	print(euro_real)
	print(dolar_real)
	print(btc_real)

	
	df = pd.DataFrame({'Moedas':['Euro','Dollar','bitcoin'],'Valores':[euro_real,dolar_real,btc_real]})
	df.to_csv("valores.csv",index=False, sep=";", decimal = ",")

	print("Arquivo exportado com sucesso para a pasta do projeto")

	
