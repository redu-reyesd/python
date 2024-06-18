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
        "# Regex\n",
        "\n",
        "## Operadores\n",
        "- **[ ]** Este operador se utiliza para crear grupos de caracteres.\n",
        "- **|** Operador or, se utiza para especificar cuando hay mas de una posibilidad de match dentro de un grupo de busqueda.\n",
        "- **^** Se utiliza para negar un set de caracteres, por ejemplo supongamos que queremos seleccionar los caracteres especiales en un parrafo.\n",
        "- **{}** se utiliza para indicar que el resultado que estamos buscando debe de coincidir ***n*** cantidad de veces.\n",
        "- **\\s** seleccionas espacios en blanco.\n",
        "- **\\S** Selecciona todo excepto los espacion en blanco.\n",
        "- **\\w** Selecciona cualquier caracter 0-9 a-z A-Z.\n",
        "- **\\W** Selecciona caracteres especiales y espacios.\n",
        "- **\\d** Selecciona digitos.\n",
        "- **\\D** Selecciona cualquier tipo de caracter y omite los digitos.\n",
        "- **\\b** Limite de Paralabra, usos:\n",
        "  - Al comienzo de la cadena, si el primer carácter de cadena es un carácter de palabra \\w.\n",
        "  - Entre dos caracteres en la cadena, donde uno es un carácter de palabra \\w y el otro no.\n",
        "  - Al final de la cadena, si el último carácter de la cadena es un carácter de palabra \\w.\n",
        "\n",
        "## Operadores especial\n",
        "- **\\n**\tnueva linea.\n",
        "- **\\t**\tSeleciona tabs.\n",
        "- **\\r**\tNormalmente se usa en combinacion con *\\n* y denota una nueva linea. Ejem *'some text\\r\\n'*.\n"
      ],
      "metadata": {
        "id": "vDeS1GFAVWLQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import regex as re\n",
        "import pandas as pd\n"
      ],
      "metadata": {
        "id": "vn0_KG1Wiob9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Buscando palabras**\n",
        "Dado el siguiente texto selecciones las palabras bananas y manzanas:\n",
        "\n",
        "- *'La manzana es roja, la banana es amarilla, y el limón es verde.'*\n",
        "\n"
      ],
      "metadata": {
        "id": "WcCuj7n5ppJA"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**esta es una instruccion**"
      ],
      "metadata": {
        "id": "IN0f7L-omTFr"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Paso 1:\n",
        "- importe la libreria regex.\n",
        "- Amacene el texto anterior en una variable."
      ],
      "metadata": {
        "id": "e-To6XRJrEdP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import regex as re\n",
        "texto='La manzana es roja, la banana es amarilla, y el limón es verde.'"
      ],
      "metadata": {
        "id": "EbEb1e8aqggq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Paso 2:\n",
        "- Cree un patron de busqueda toman en consideracion la funcion de cada operador\n"
      ],
      "metadata": {
        "id": "yEegg22brX47"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# declare un variable para almacenar el patron de busqueda\n",
        "patron_de_busqueda= re.compile(r'\\b[r,b,m,a,v]\\w+\\b')\n",
        "# realice la busqueda del patron dentro del texto\n",
        "lista_de_resultados=patron_de_busqueda.findall(texto)\n",
        "print(lista_de_resultados)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sLBPPTpbrlvi",
        "outputId": "c62786ca-26ff-46a3-efe5-e59cffb6dff1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['manzana', 'roja', 'banana', 'amarilla', 'verde']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### identificar interfaces  de un router:\n",
        "\n",
        "```bash\n",
        "Python360YT#show running-config | include hostname\n",
        "hostname Python360YT\n",
        "Python360YT#show ip in bri\n",
        "Python360YT#show ip in brief\n",
        "Interface              IP-Address      OK? Method Status                Protocol\n",
        "GigabitEthernet1       10.10.20.48     YES NVRAM  up                    up\n",
        "GigabitEthernet2       192.168.10.4    YES manual up                    up\n",
        "GigabitEthernet3       unassigned      YES NVRAM  administratively down down\n",
        "Loopback0              10.0.0.1        YES NVRAM  up                    up\n",
        "Loopback1              172.1.1.1       YES manual up                    up\n",
        "Loopback10             unassigned      YES unset  up                    up\n",
        "Loopback20             172.168.1.1     YES manual up                    up\n",
        "Loopback21             172.168.10.1    YES manual up                    up\n",
        "Loopback42             2.3.3.6         YES other  up                    up\n",
        "Loopback56             56.56.56.56     YES manual up                    up\n",
        "Loopback98             172.16.98.1     YES manual up                    up\n",
        "Loopback99             172.16.1.1      YES manual up                    up\n",
        "VirtualPortGroup0      192.168.1.1     YES NVRAM  up                    up\n",
        "Vlan10                 192.168.110.2   YES manual down                  down\n",
        "Vlan20                 192.168.120.1   YES manual down                  down\n",
        "Vlan30                 192.168.130.1   YES manual down                  down\n",
        "Python360YT#\n",
        "```\n",
        "```bash\n",
        "Python361YT#show running-config | include hostname\n",
        "hostname Python360YT\n",
        "Python361YT#show ip in bri\n",
        "Python361YT#show ip in brief\n",
        "Interface              IP-Address      OK? Method Status                Protocol\n",
        "GigabitEthernet1       10.10.20.48     YES NVRAM  up                    up\n",
        "GigabitEthernet2       unassigned      YES manual administratively down down\n",
        "GigabitEthernet3       192.168.10.4    YES NVRAM  up                    up\n",
        "Loopback0              10.0.0.1        YES NVRAM  up                    up\n",
        "Loopback1              172.1.1.1       YES manual up                    up\n",
        "Loopback10             unassigned      YES unset  up                    up\n",
        "Loopback20             172.168.1.1     YES manual up                    up\n",
        "Loopback21             172.168.10.1    YES manual up                    up\n",
        "Loopback42             2.3.3.6         YES other  up                    up\n",
        "Loopback56             56.56.56.56     YES manual up                    up\n",
        "Loopback98             172.16.98.1     YES manual up                    up\n",
        "Loopback99             172.16.1.1      YES manual up                    up\n",
        "VirtualPortGroup0      192.168.1.1     YES NVRAM  up                    up\n",
        "Vlan10                 192.168.110.2   YES manual down                  down\n",
        "Vlan20                 192.168.120.1   YES manual down                  down\n",
        "Vlan30                 192.168.130.1   YES manual down                  down\n",
        "Python361YT#\n",
        "```\n"
      ],
      "metadata": {
        "id": "dk75Ov-EtXb7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "r1='''Python360YT#show running-config | include hostname\n",
        "hostname Python360YT\n",
        "Python360YT#show ip in bri\n",
        "Python360YT#show ip in brief\n",
        "Interface              IP-Address      OK? Method Status                Protocol\n",
        "GigabitEthernet1       10.10.20.48     YES NVRAM  up                    up\n",
        "GigabitEthernet2       192.168.10.4    YES manual up                    up\n",
        "GigabitEthernet3       unassigned      YES NVRAM  administratively down down\n",
        "Loopback0              10.0.0.1        YES NVRAM  up                    up\n",
        "Loopback1              172.1.1.1       YES manual up                    up\n",
        "Loopback10             unassigned      YES unset  up                    up\n",
        "Loopback20             172.168.1.1     YES manual up                    up\n",
        "Loopback21             172.168.10.1    YES manual up                    up\n",
        "Loopback42             2.3.3.6         YES other  up                    up\n",
        "Loopback56             56.56.56.56     YES manual up                    up\n",
        "Loopback98             172.16.98.1     YES manual up                    up\n",
        "Loopback99             172.16.1.1      YES manual up                    up\n",
        "VirtualPortGroup0      192.168.1.1     YES NVRAM  up                    up\n",
        "Vlan10                 192.168.110.2   YES manual down                  down\n",
        "Vlan20                 192.168.120.1   YES manual down                  down\n",
        "Vlan30                 192.168.130.1   YES manual down                  down\n",
        "Python360YT#'''\n",
        "r2='''Python361YT#show running-config | include hostname\n",
        "hostname Python361YT\n",
        "Python361YT#show ip in bri\n",
        "Python361YT#show ip in brief\n",
        "Interface              IP-Address      OK? Method Status                Protocol\n",
        "GigabitEthernet1       10.10.20.48     YES NVRAM  up                    up\n",
        "GigabitEthernet2       unassigned      YES manual administratively down down\n",
        "GigabitEthernet3       192.168.10.4    YES NVRAM  up                    up\n",
        "Loopback0              10.0.0.1        YES NVRAM  up                    up\n",
        "Loopback1              172.1.1.1       YES manual up                    up\n",
        "Loopback10             unassigned      YES unset  up                    up\n",
        "Loopback20             172.168.1.1     YES manual up                    up\n",
        "Loopback21             172.168.10.1    YES manual up                    up\n",
        "Loopback42             2.3.3.6         YES other  up                    up\n",
        "Loopback56             56.56.56.56     YES manual up                    up\n",
        "Loopback98             172.16.98.1     YES manual up                    up\n",
        "Loopback99             172.16.1.1      YES manual up                    up\n",
        "VirtualPortGroup0      192.168.1.1     YES NVRAM  up                    up\n",
        "Vlan10                 192.168.110.2   YES manual down                  down\n",
        "Vlan20                 192.168.120.1   YES manual down                  down\n",
        "Vlan30                 192.168.130.1   YES manual down                  down\n",
        "Python361YT#'''"
      ],
      "metadata": {
        "id": "DwD77ZZcySSS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Obtener nombre de los routers\n",
        "itere entre ambas variables y obtenga el nombre de cada router\n",
        "\n",
        "para obtener el nombre considere la siguiente lista de operadore:\n",
        "- **\\b**\n",
        "- **[ ]**\n",
        "- **\\w**\n",
        "- **+**\n",
        "\n",
        "cree un patron para identificar los nombre de cada equipo y cree una lista"
      ],
      "metadata": {
        "id": "WIWm3Jd-zYYW"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Defina el patron de busqueda"
      ],
      "metadata": {
        "id": "piDwailX101n"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "patron=re.compile(r'\\bPython\\w+\\b')"
      ],
      "metadata": {
        "id": "DGmdBrj914cN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "forma extendida"
      ],
      "metadata": {
        "id": "h2s5xn0V1WQD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "lista_de_equipos=[]\n",
        "for item in (r1,r2):\n",
        "  nombre=patron.findall(item)\n",
        "  lista_de_equipos.append(nombre)\n",
        "print([list(set(x))[0] for x in lista_de_equipos])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BZlZL5aW0TrK",
        "outputId": "bf9c609d-3d16-4fd2-ce4b-24f17213132a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Python360YT', 'Python361YT']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "forma comprimida"
      ],
      "metadata": {
        "id": "5W7vmkaP1qzd"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "lista_de_equipos=[]\n",
        "for item in (r1,r2):\n",
        "  lista_de_equipos.append(patron.findall(item))\n",
        "print([list(set(x))[0] for x in lista_de_equipos])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GWII2HRSyn6v",
        "outputId": "60975138-4bf0-4791-97fd-1cdaa6bd6a65"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Python360YT', 'Python361YT']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "List comprehenssion:"
      ],
      "metadata": {
        "id": "z-ZTrzQZ180t"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "lista_de_equipos=[ list(set(patron.findall(item)))[0] if patron.findall(item) else '' for item in (r1,r2)]"
      ],
      "metadata": {
        "id": "EikqxnLh2Ati"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Verifique el valor de la variable lista_de_equipos"
      ],
      "metadata": {
        "id": "Lrmwhzso2evg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "lista_de_equipos"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4DNJ4HJn2Kyy",
        "outputId": "727c4f78-8c13-47d8-e603-360b5274ed66"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Python360YT', 'Python361YT']"
            ]
          },
          "metadata": {},
          "execution_count": 68
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Crear un patron de busqueda para interfaces y direcciones ip\n",
        "\n",
        "- cree un patron de busqueda que le permite identificar hostname, interfaz y direcccion ip\n",
        "- Tome el output y seperalo por lineas.\n",
        "- cree un diccionario con los resultado\n",
        "- cree un dataframe con ese diccionario\n",
        "- finalmente escriba el dataframe a un archivo csv"
      ],
      "metadata": {
        "id": "lNXSV1I1yAx1"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "reporte={\n",
        "         'Host Name':[],\n",
        "         'Interface Id':[],\n",
        "         'Ip Address':[]}\n",
        "\n",
        "\n",
        "interfaces_ip=re.compile(r'(\\S+)\\s+(\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}|unassigned)')\n",
        "for item in (r1,r2):\n",
        "           #split items by lines\n",
        "  for x in item.splitlines():\n",
        "    data=interfaces_ip.findall(x)\n",
        "    if data:\n",
        "      reporte['Host Name'].append(list(set(patron.findall(item)))[0])\n",
        "      reporte['Interface Id'].append(data[0][0])\n",
        "      reporte['Ip Address'].append(data[0][1])\n",
        "\n"
      ],
      "metadata": {
        "id": "-t2W4GAcyNi_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "Data_reporte = pd.DataFrame(reporte)\n"
      ],
      "metadata": {
        "id": "3XO34oerzPyD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "Data_reporte"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "H9FfTJy60eC_",
        "outputId": "32cb0f85-e68f-4cd3-81a1-1aaf08f4a880"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "      Host Name       Interface Id     Ip Address\n",
              "0   Python360YT   GigabitEthernet1    10.10.20.48\n",
              "1   Python360YT   GigabitEthernet2   192.168.10.4\n",
              "2   Python360YT   GigabitEthernet3     unassigned\n",
              "3   Python360YT          Loopback0       10.0.0.1\n",
              "4   Python360YT          Loopback1      172.1.1.1\n",
              "5   Python360YT         Loopback10     unassigned\n",
              "6   Python360YT         Loopback20    172.168.1.1\n",
              "7   Python360YT         Loopback21   172.168.10.1\n",
              "8   Python360YT         Loopback42        2.3.3.6\n",
              "9   Python360YT         Loopback56    56.56.56.56\n",
              "10  Python360YT         Loopback98    172.16.98.1\n",
              "11  Python360YT         Loopback99     172.16.1.1\n",
              "12  Python360YT  VirtualPortGroup0    192.168.1.1\n",
              "13  Python360YT             Vlan10  192.168.110.2\n",
              "14  Python360YT             Vlan20  192.168.120.1\n",
              "15  Python360YT             Vlan30  192.168.130.1\n",
              "16  Python361YT   GigabitEthernet1    10.10.20.48\n",
              "17  Python361YT   GigabitEthernet2     unassigned\n",
              "18  Python361YT   GigabitEthernet3   192.168.10.4\n",
              "19  Python361YT          Loopback0       10.0.0.1\n",
              "20  Python361YT          Loopback1      172.1.1.1\n",
              "21  Python361YT         Loopback10     unassigned\n",
              "22  Python361YT         Loopback20    172.168.1.1\n",
              "23  Python361YT         Loopback21   172.168.10.1\n",
              "24  Python361YT         Loopback42        2.3.3.6\n",
              "25  Python361YT         Loopback56    56.56.56.56\n",
              "26  Python361YT         Loopback98    172.16.98.1\n",
              "27  Python361YT         Loopback99     172.16.1.1\n",
              "28  Python361YT  VirtualPortGroup0    192.168.1.1\n",
              "29  Python361YT             Vlan10  192.168.110.2\n",
              "30  Python361YT             Vlan20  192.168.120.1\n",
              "31  Python361YT             Vlan30  192.168.130.1"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-00754a4e-1eb6-4520-9681-8914da367d27\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Host Name</th>\n",
              "      <th>Interface Id</th>\n",
              "      <th>Ip Address</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Python360YT</td>\n",
              "      <td>GigabitEthernet1</td>\n",
              "      <td>10.10.20.48</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Python360YT</td>\n",
              "      <td>GigabitEthernet2</td>\n",
              "      <td>192.168.10.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Python360YT</td>\n",
              "      <td>GigabitEthernet3</td>\n",
              "      <td>unassigned</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Python360YT</td>\n",
              "      <td>Loopback0</td>\n",
              "      <td>10.0.0.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Python360YT</td>\n",
              "      <td>Loopback1</td>\n",
              "      <td>172.1.1.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>Python360YT</td>\n",
              "      <td>Loopback10</td>\n",
              "      <td>unassigned</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>Python360YT</td>\n",
              "      <td>Loopback20</td>\n",
              "      <td>172.168.1.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>Python360YT</td>\n",
              "      <td>Loopback21</td>\n",
              "      <td>172.168.10.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>Python360YT</td>\n",
              "      <td>Loopback42</td>\n",
              "      <td>2.3.3.6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>Python360YT</td>\n",
              "      <td>Loopback56</td>\n",
              "      <td>56.56.56.56</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>Python360YT</td>\n",
              "      <td>Loopback98</td>\n",
              "      <td>172.16.98.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>Python360YT</td>\n",
              "      <td>Loopback99</td>\n",
              "      <td>172.16.1.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>Python360YT</td>\n",
              "      <td>VirtualPortGroup0</td>\n",
              "      <td>192.168.1.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>13</th>\n",
              "      <td>Python360YT</td>\n",
              "      <td>Vlan10</td>\n",
              "      <td>192.168.110.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>Python360YT</td>\n",
              "      <td>Vlan20</td>\n",
              "      <td>192.168.120.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>15</th>\n",
              "      <td>Python360YT</td>\n",
              "      <td>Vlan30</td>\n",
              "      <td>192.168.130.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16</th>\n",
              "      <td>Python361YT</td>\n",
              "      <td>GigabitEthernet1</td>\n",
              "      <td>10.10.20.48</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>17</th>\n",
              "      <td>Python361YT</td>\n",
              "      <td>GigabitEthernet2</td>\n",
              "      <td>unassigned</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18</th>\n",
              "      <td>Python361YT</td>\n",
              "      <td>GigabitEthernet3</td>\n",
              "      <td>192.168.10.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>19</th>\n",
              "      <td>Python361YT</td>\n",
              "      <td>Loopback0</td>\n",
              "      <td>10.0.0.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>20</th>\n",
              "      <td>Python361YT</td>\n",
              "      <td>Loopback1</td>\n",
              "      <td>172.1.1.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>21</th>\n",
              "      <td>Python361YT</td>\n",
              "      <td>Loopback10</td>\n",
              "      <td>unassigned</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>22</th>\n",
              "      <td>Python361YT</td>\n",
              "      <td>Loopback20</td>\n",
              "      <td>172.168.1.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>23</th>\n",
              "      <td>Python361YT</td>\n",
              "      <td>Loopback21</td>\n",
              "      <td>172.168.10.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>24</th>\n",
              "      <td>Python361YT</td>\n",
              "      <td>Loopback42</td>\n",
              "      <td>2.3.3.6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25</th>\n",
              "      <td>Python361YT</td>\n",
              "      <td>Loopback56</td>\n",
              "      <td>56.56.56.56</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>26</th>\n",
              "      <td>Python361YT</td>\n",
              "      <td>Loopback98</td>\n",
              "      <td>172.16.98.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>27</th>\n",
              "      <td>Python361YT</td>\n",
              "      <td>Loopback99</td>\n",
              "      <td>172.16.1.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>28</th>\n",
              "      <td>Python361YT</td>\n",
              "      <td>VirtualPortGroup0</td>\n",
              "      <td>192.168.1.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29</th>\n",
              "      <td>Python361YT</td>\n",
              "      <td>Vlan10</td>\n",
              "      <td>192.168.110.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>30</th>\n",
              "      <td>Python361YT</td>\n",
              "      <td>Vlan20</td>\n",
              "      <td>192.168.120.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>31</th>\n",
              "      <td>Python361YT</td>\n",
              "      <td>Vlan30</td>\n",
              "      <td>192.168.130.1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-00754a4e-1eb6-4520-9681-8914da367d27')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-00754a4e-1eb6-4520-9681-8914da367d27 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-00754a4e-1eb6-4520-9681-8914da367d27');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-9005d1ac-9e84-4693-ad30-a27fa7c4935a\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-9005d1ac-9e84-4693-ad30-a27fa7c4935a')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-9005d1ac-9e84-4693-ad30-a27fa7c4935a button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "  <div id=\"id_2a6d6a64-4684-4609-8aa4-70c033df251c\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('Data_reporte')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_2a6d6a64-4684-4609-8aa4-70c033df251c button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('Data_reporte');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "Data_reporte",
              "summary": "{\n  \"name\": \"Data_reporte\",\n  \"rows\": 32,\n  \"fields\": [\n    {\n      \"column\": \"Host Name\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Python361YT\",\n          \"Python360YT\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Interface Id\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 16,\n        \"samples\": [\n          \"GigabitEthernet1\",\n          \"GigabitEthernet2\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Ip Address\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 15,\n        \"samples\": [\n          \"172.16.98.1\",\n          \"192.168.1.1\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 93
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "xDW68Tr46wCf"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}