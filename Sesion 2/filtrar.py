import pandas as pd
import os
peliculas = pd.read_csv('./csvs/netflix_titles.csv',
                        usecols=[0,5],
                        names=['Show ID','Pais'],
                        header=0
                        )

peliculas.dropna(inplace=True)
print(peliculas)
pelis_usa=peliculas[peliculas['Pais']=='United States']
print(pelis_usa)
pelis_usa.to_csv('./csvs/reporte.csv')
pelis_usa.to_json('./csvs/reporte.json')

for id in pelis_usa.index:
    print(f'Show id : {pelis_usa["Show ID"][id]} Pais {pelis_usa["Pais"][id]}')   
    print('################################')