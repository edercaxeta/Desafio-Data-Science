import pandas as pd

uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"

filmes = pd.read_csv(uri)

filme_id_32 = filmes[filmes['movieId'] == 32]

if filme_id_32['rating'].mean() > 3:
    print(f"O filme com ID 32 é bom, com uma nota média de {filme_id_32['rating'].mean():.2f}")
else:
    print(f"O filme com ID 32 não é considerado bom, com uma nota média de {filme_id_32['rating'].mean():.2f}")
