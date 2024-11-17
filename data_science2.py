import pandas as pd
uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"

pd.read_csv(uri)

filmes = pd.read_csv(uri)

##filmes.head(12)

##print(filmes.tail(6))

filmes.size