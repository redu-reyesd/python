{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "# PANDAS\n",
        "  \n",
        "Pandas es una librería de Python para análisis de datos, esencial para trabajar con estructuras tabulares como DataFrames. Facilita tareas como limpieza, filtrado y análisis exploratorio de datos, siendo fundamental para científicos de datos y analistas.\n",
        "\n",
        "## Uso de DataFrames y Series en Pandas para manipular y analizar datos."
      ],
      "metadata": {
        "id": "zMpm87d7b-FT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "import pandas as pd\n",
        "\n",
        "# Crear un DataFrame directamente\n",
        "df = pd.DataFrame({\n",
        "    'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],\n",
        "    'Edad': [25, 30, 35, 40],\n",
        "    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']\n",
        "})\n",
        "\n",
        "# Mostrar el DataFrame\n",
        "print(df)\n",
        "\n",
        "# Mostrar solo la columna de edades\n",
        "print(df['Edad'])\n"
      ],
      "metadata": {
        "id": "w_UY8FFndQvj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Filtrado, limpieza y transformación de datos utilizando Pandas.\n",
        "\n"
      ],
      "metadata": {
        "id": "mT8DyBzsdXtM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "# Crear un DataFrame directamente\n",
        "df = pd.DataFrame({\n",
        "    'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],\n",
        "    'Edad': [25, 30, 35, 40],\n",
        "    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']\n",
        "})\n",
        "\n",
        "# Mostrar el DataFrame\n",
        "print(df)\n",
        "\n",
        "# Mostrar solo la columna de edades\n",
        "print(df['Edad'])\n",
        "\n",
        "# Filtrar personas mayores de 30 años\n",
        "print(df[df['Edad'] > 30])"
      ],
      "metadata": {
        "id": "_cFaJ_0xdqO6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Eliminar filas con valores nulos\n",
        "El método dropna permite, de una forma muy conveniente, filtrar los valores de una estructura de datos pandas para dejar solo aquellos no nulos.\n",
        "```python\n",
        "# Eliminar filas con valores nulos\n",
        "df.dropna(inplace=True)\n",
        "```\n",
        "## Tambien se puden realizar otro tipo de operaciones como las siguientes:\n",
        "\n",
        "```python\n",
        "# Calcular el total de ventas por producto\n",
        "df['Total Ventas'] = df['Cantidad Vendida'] * df['Precio Unitario']\n",
        "# Filtrar productos con ventas totales mayores a 1000\n",
        "df_filtrado = df[df['Total Ventas'] > 1000]\n",
        "# Mostrar DataFrame con productos filtrados\n",
        "print(df_filtrado)\n",
        "```"
      ],
      "metadata": {
        "id": "eXZTJhBsd4BE"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "pY41pLq8d74s"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Importe un datase a Python\n",
        "\n",
        "para ello puede hacer uso del metodo read_csv()\n",
        "\n",
        "Argumentos:\n",
        "- './pokemon_data.csv'\n",
        "- usecols: Columnas del CSV que queremos extraer(tome en consideración que la primera columna seria la columna 0), ejmpl usecols=[0,1,2,3,4]\n",
        "- names, Como quiere mostrar los bombre de cada columna ejemple names=['Id','Name','Generacion','type1','type2'].\n",
        "Si no desea modificar el nombre de las cabeceras entonces excluya este argumento\n",
        "- header, Indica en que linea inician las cabeceras,\n",
        "-  - posible valores:\n",
        "- -  - header=None\n",
        "\n",
        "| Id    | Name       | Generacion | Type1 | Type2 |\n",
        "|-------|------------|------------|-------|-------|\n",
        "| dexnum| name       | generation | type1 | type2 |\n",
        "| 0001  | Bulbasaur  | 1          | Grass | Poison|\n",
        "    \n",
        "-  -  - header=0\n",
        "\n",
        "| Id    | Name       | Generacion | Type1 | Type2 |\n",
        "|-------|------------|------------|-------|-------|\n",
        "| 0001  | Bulbasaur  | 1          | Grass | Poison|\n",
        "\n",
        "\n",
        "<cite> Nota: No indecar el parametro header tiene el mismo efecto que usar header=None</cite>"
      ],
      "metadata": {
        "id": "skPNmzWffWVD"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 25,
      "metadata": {
        "id": "vLtAzwFQg3up"
      },
      "outputs": [],
      "source": [
        "\n",
        "import pandas as pd\n",
        "csv_file='/content/drive/MyDrive/Pandas/pokemon_data.csv'\n",
        "df = pd.read_csv(csv_file,\n",
        "                 usecols=[0,1,2,3,4],\n",
        "                 names=['Id','Name','Generacion','type1','type2'],\n",
        "                 header=0)\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Para vizualizar el contenido del dataframe pude utilizar el comando print\n",
        "```python\n",
        "print(df)\n",
        "```"
      ],
      "metadata": {
        "id": "5271vMPCnHQj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(df)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5H9ec4utiF9i",
        "outputId": "fbef0199-9e95-4e5f-b78f-db7f8cf99a38"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "        Id          Name  Generacion     type1    type2\n",
            "0        1     Bulbasaur           1     Grass   Poison\n",
            "1        2       Ivysaur           1     Grass   Poison\n",
            "2        3      Venusaur           1     Grass   Poison\n",
            "3        4    Charmander           1      Fire      NaN\n",
            "4        5    Charmeleon           1      Fire      NaN\n",
            "...    ...           ...         ...       ...      ...\n",
            "1020  1021   Raging Bolt           9  Electric   Dragon\n",
            "1021  1022  Iron Boulder           9      Rock  Psychic\n",
            "1022  1023    Iron Crown           9     Steel  Psychic\n",
            "1023  1024     Terapagos           9    Normal      NaN\n",
            "1024  1025     Pecharunt           9    Poison    Ghost\n",
            "\n",
            "[1025 rows x 5 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Pandas\n",
        "\n",
        "Crear un daframe a partir de un diccionario\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "ZC3nNBOvjh8N"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n"
      ],
      "metadata": {
        "id": "us8_mjk2iH19"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "Crear un DataFrame a partir de un archivo CSV y luego filtrarlo\n",
        "https://www.kaggle.com/datasets/guavocado/pokemon-stats-1025-pokemons?select=pokemon_data.csv"
      ],
      "metadata": {
        "id": "jEmxXrnUnqwx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Cree un dataframe en python utilizando dataset publicos, en las siguientes paginas puede encontrar datasets publicos:\n",
        "\n",
        "- https://365datascience.com/tutorials/python-tutorials/free-public-datasets-python/\n",
        "\n",
        "- www.kaggle.com\n",
        "\n",
        "Tambien puede hacer uso de los dataset en el siguiente directorio ./datasets"
      ],
      "metadata": {
        "id": "b1MC3Y1mnxPF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "import pandas as pd\n",
        "import os\n",
        "\n",
        "csv_file='/content/drive/MyDrive/Pandas/netflix_titles.csv'\n",
        "peliculas = pd.read_csv(csv_file,\n",
        "                        usecols=[0,5],\n",
        "                        names=['Show ID','Pais'],\n",
        "                        header=0\n",
        "                        )\n",
        "'''\n",
        "  verifica si un directorio existe o no existe\n",
        "  si el directorio no existe entonces lo crea, notese que estamos utilizando\n",
        "  una negacion para ahorrarnos la line del else, asi las cosas si el directorio existe nos devolveria\n",
        "  un False razon por la cual no entraria al if; pero si el directorio no existe nos deviolveria true\n",
        "  y entraria al if y porteriormente ejecutaria la linea os.mkdir('./reporte')\n",
        "'''\n",
        "if not (os.path.exists('./reporte')):\n",
        "  os.mkdir('./reporte')\n",
        "\n",
        "# Filtra los espacion en blanco o Nulos\n",
        "peliculas.dropna(inplace=True)\n",
        "print(peliculas)\n",
        "\n",
        "#filtra las peliculas por pais\n",
        "\n",
        "pelis_usa=peliculas[peliculas['Pais']=='United States']\n",
        "print(pelis_usa)\n",
        "#guarda un reporte en formato csv\n",
        "pelis_usa.to_csv('./reporte/reporte.csv')\n",
        "#guarda un reporte en formato json\n",
        "pelis_usa.to_json('./reporte/reporte.json')\n",
        "\n",
        "for id in pelis_usa.index:\n",
        "    print(f'Show id : {pelis_usa[\"Show ID\"][id]} Pais {pelis_usa[\"Pais\"][id]}')\n",
        "    print('################################')"
      ],
      "metadata": {
        "id": "S80mx37_oVpT"
      },
      "execution_count": 30,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Enlaces de interes\n",
        "\n",
        "https://medium.com/@MargrietGr/analyze-open-data-sets-using-pandas-in-a-python-notebook-64e93776370a\n",
        "\n",
        "https://interactivechaos.com/es/manual/tutorial-de-pandas/el-metodo-dropna\n",
        "\n",
        "https://www.geeksforgeeks.org/pandas-tutorial/?ref=header_search\n",
        "\n",
        "https://www.w3schools.com/python/pandas/default.asp"
      ],
      "metadata": {
        "id": "W7ketGPwoW-b"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "7MsMKOEapwxQ"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}