import pandas as pd ## Biblioteca de análise de dados

## Abaixo lemos o arquivo e colocamos os dados na memória principal
movies = pd.read_csv("mymoviedb.csv",lineterminator='\n')

## O comando head nos permite observar parcialmente o conteúdo da base da dados, com destaque para as colunas existentes
movies.head(15)

## O comando unique nos retorna os valores unicos de uma determinada coluna
movies["Original_Language"].unique()

## O comando describe nos da algumas informacoes acerca de algumas medidas estatisticas 
movies.describe()

## O comando verifica a frequência com o qual os valores se repetem
movies.value_counts("Original_Language")