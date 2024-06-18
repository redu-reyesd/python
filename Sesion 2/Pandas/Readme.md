
# PANDAS

Pandas es una librería de Python para análisis de datos, esencial para
trabajar con estructuras tabulares como DataFrames. Facilita tareas como
limpieza, filtrado y análisis exploratorio de datos, siendo fundamental
para científicos de datos y analistas.

## Uso de DataFrames y Series en Pandas para manipular y analizar datos. {#uso-de-dataframes-y-series-en-pandas-para-manipular-y-analizar-datos}

``` python

import pandas as pd

# Crear un DataFrame directamente
df = pd.DataFrame({
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
    'Edad': [25, 30, 35, 40],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']
})

# Mostrar el DataFrame
print(df)

# Mostrar solo la columna de edades
print(df['Edad'])
```

# Filtrado, limpieza y transformación de datos utilizando Pandas. {#filtrado-limpieza-y-transformación-de-datos-utilizando-pandas}

``` python
import pandas as pd

# Crear un DataFrame directamente
df = pd.DataFrame({
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
    'Edad': [25, 30, 35, 40],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']
})

# Mostrar el DataFrame
print(df)

# Mostrar solo la columna de edades
print(df['Edad'])

# Filtrar personas mayores de 30 años
print(df[df['Edad'] > 30])
```

## Eliminar filas con valores nulos

El método dropna permite, de una forma muy conveniente, filtrar los
valores de una estructura de datos pandas para dejar solo aquellos no
nulos.

``` python
# Eliminar filas con valores nulos
df.dropna(inplace=True)
```

## Tambien se puden realizar otro tipo de operaciones como las siguientes:

``` python
# Calcular el total de ventas por producto
df['Total Ventas'] = df['Cantidad Vendida'] * df['Precio Unitario']
# Filtrar productos con ventas totales mayores a 1000
df_filtrado = df[df['Total Ventas'] > 1000]
# Mostrar DataFrame con productos filtrados
print(df_filtrado)
```


# Importe un datase a Python

para ello puede hacer uso del metodo read_csv()

Argumentos:

-   './pokemon_data.csv'

-   usecols: Columnas del CSV que queremos extraer(tome en consideración
    que la primera columna seria la columna 0), ejmpl
    usecols=[0,1,2,3,4]

-   names, Como quiere mostrar los bombre de cada columna ejemple
    names=['Id','Name','Generacion','type1','type2']. Si no
    desea modificar el nombre de las cabeceras entonces excluya este
    argumento

-   header, Indica en que linea inician las cabeceras,

-   -   posible valores:

-   -   -   header=None

| Id    | Name       | Generacion | Type1 | Type2 |
|-------|------------|------------|-------|-------|
| dexnum| name       | generation | type1 | type2 |
| 0001  | Bulbasaur  | 1          | Grass | Poison|
    

-   -   -   header=0

| Id    | Name       | Generacion | Type1 | Type2 |
|-------|------------|------------|-------|-------|
| 0001  | Bulbasaur  | 1          | Grass | Poison|


<cite> Nota: No indecar el parametro header tiene el mismo
efecto que usar header=None</cite>

``` python

import pandas as pd
csv_file='/content/drive/MyDrive/Pandas/pokemon_data.csv'
df = pd.read_csv(csv_file,
                 usecols=[0,1,2,3,4],
                 names=['Id','Name','Generacion','type1','type2'],
                 header=0)

```

Para vizualizar el contenido del dataframe pude utilizar el comando
print

``` python
print(df)
```



            Id          Name  Generacion     type1    type2
    0        1     Bulbasaur           1     Grass   Poison
    1        2       Ivysaur           1     Grass   Poison
    2        3      Venusaur           1     Grass   Poison
    3        4    Charmander           1      Fire      NaN
    4        5    Charmeleon           1      Fire      NaN
    ...    ...           ...         ...       ...      ...
    1020  1021   Raging Bolt           9  Electric   Dragon
    1021  1022  Iron Boulder           9      Rock  Psychic
    1022  1023    Iron Crown           9     Steel  Psychic
    1023  1024     Terapagos           9    Normal      NaN
    1024  1025     Pecharunt           9    Poison    Ghost

    [1025 rows x 5 columns]



# Pandas {#pandas}

Crear un daframe a partir de un diccionario

``` python
import pandas as pd
```

``` python
Crear un DataFrame a partir de un archivo CSV y luego filtrarlo
https://www.kaggle.com/datasets/guavocado/pokemon-stats-1025-pokemons?select=pokemon_data.csv
```

Cree un dataframe en python utilizando dataset publicos, en las
siguientes paginas puede encontrar datasets publicos:

-   <https://365datascience.com/tutorials/python-tutorials/free-public-datasets-python/>

-   www.kaggle.com

Tambien puede hacer uso de los dataset en el siguiente directorio
./datasets

``` python

import pandas as pd
import os

csv_file='/content/drive/MyDrive/Pandas/netflix_titles.csv'
peliculas = pd.read_csv(csv_file,
                        usecols=[0,5],
                        names=['Show ID','Pais'],
                        header=0
                        )
'''
  verifica si un directorio existe o no existe
  si el directorio no existe entonces lo crea, notese que estamos utilizando
  una negacion para ahorrarnos la line del else, asi las cosas si el directorio existe nos devolveria
  un False razon por la cual no entraria al if; pero si el directorio no existe nos deviolveria true
  y entraria al if y porteriormente ejecutaria la linea os.mkdir('./reporte')
'''
if not (os.path.exists('./reporte')):
  os.mkdir('./reporte')

# Filtra los espacion en blanco o Nulos
peliculas.dropna(inplace=True)
print(peliculas)

#filtra las peliculas por pais

pelis_usa=peliculas[peliculas['Pais']=='United States']
print(pelis_usa)
#guarda un reporte en formato csv
pelis_usa.to_csv('./reporte/reporte.csv')
#guarda un reporte en formato json
pelis_usa.to_json('./reporte/reporte.json')

for id in pelis_usa.index:
    print(f'Show id : {pelis_usa["Show ID"][id]} Pais {pelis_usa["Pais"][id]}')
    print('################################')
```

# Enlaces de interes

<https://medium.com/@MargrietGr/analyze-open-data-sets-using-pandas-in-a-python-notebook-64e93776370a>

<https://interactivechaos.com/es/manual/tutorial-de-pandas/el-metodo-dropna>

<https://www.geeksforgeeks.org/pandas-tutorial/?ref=header_search>

<https://www.w3schools.com/python/pandas/default.asp>

