import pandas as pd
uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv"

pd.read_csv(uri)

filmes = pd.read_csv(uri)

##filmes.head(5)

filmes.size