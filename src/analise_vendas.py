#IMPORTAÇÃO

import pandas as pd #importando o pandas

#LEITURA DO CSV

df = pd.read_csv("dados/vendas.csv") #Le o arquivo CSV e armazena os dados em um DataFrame

#EXPLORAÇÃO DOS DADOS

print(df.head()) #mostrar previa dos dados da tabela pois e um arquivo grande

print(df.shape) #mostra quantas linhas e colunas possui o dataframe

print(df.shape[0]) #mostra linhas do dataframe

print(df.shape[1]) #mostra colunas do dataframe

print(df.columns) #mostra nome das colunas do dataframe

print(df.tail()) #mostra as últimas linhas do dataframe

print(df.dtypes) #mostra o tipo de cada dado armazenado nas colunas do dataframe

print(df.describe()) #descreve os dados do dataframe

print(df.info()) #mostra um resumo do dataframe

#ANÁLISES 

print(df["produto"].count()) #conta os produtos que possui no dataframe

print(df["preco_unitario"].max()) #mostra o produto com maior preço

print(df["preco_unitario"].min()) #mostra o produto com menor preço

print(df["preco_unitario"].mean()) #mostra a média dos produtos

#FILTROS

print(df[df["preco_unitario"] > 1000]["produto"]) #mostra os produtos que possuem preço maior que 1000

print(df[df["cidade"] == "São Paulo"]["produto"]) #mostra os produtos apenas da cidade de São Paulo

print(df[df["produto"] == "Notebook"]) #mostra apenas os produtos que são notebook

#ORDENAÇÃO

print(df["preco_unitario"].sort_values()) #ordena os preços dos produtos

print(df["cidade"].value_counts()) #mostra quantas vendas tiveram em cada cidade


