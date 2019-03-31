
import requests


url = "http://data.fixer.io/api/latest?access_key=3fbfd1fd46eb28d638ba12e895ce1bef"
print("Acessando Base de Dados...")
response = requests.get(url)
if response.status_code==200:
	print("Conseguiu acessar base de dados!")
	print("Buscando informações das moedas...")
	print(response)
	dados = response.json()
	print(dados['rates']['EUR'])
	print(dados['rates']['BRL'])
	print(dados['rates']['USD'])
	print(dados['rates']['BTC'])

	euro_real = dados['rates']['BRL'] / dados['rates']['EUR']
	dolar_real = dados['rates']['BRL'] / dados['rates']['USD']
	btc_real = dados['rates']['BRL'] / dados['rates']['BTC']


	print(euro_real)
	print(dolar_real)
	print(btc_real)