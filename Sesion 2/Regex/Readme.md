---
jupyter:
  colab:
  kernelspec:
    display_name: Python 3
    name: python3
  language_info:
    name: python
  nbformat: 4
  nbformat_minor: 0
---

<div class="cell markdown" id="vDeS1GFAVWLQ">

# Regex

## Operadores

-   **\[ \]** Este operador se utiliza para crear grupos de caracteres.
-   **\|** Operador or, se utiza para especificar cuando hay mas de una
    posibilidad de match dentro de un grupo de busqueda.
-   **^** Se utiliza para negar un set de caracteres, por ejemplo
    supongamos que queremos seleccionar los caracteres especiales en un
    parrafo.
-   **{}** se utiliza para indicar que el resultado que estamos buscando
    debe de coincidir ***n*** cantidad de veces.
-   **\\s** seleccionas espacios en blanco.
-   **\\S** Selecciona todo excepto los espacion en blanco.
-   **\\w** Selecciona cualquier caracter 0-9 a-z A-Z.
-   **\\W** Selecciona caracteres especiales y espacios.
-   **\\d** Selecciona digitos.
-   **\\D** Selecciona cualquier tipo de caracter y omite los digitos.
-   **\\b** Limite de Paralabra, usos:
    -   Al comienzo de la cadena, si el primer carácter de cadena es un
        carácter de palabra \\w.
    -   Entre dos caracteres en la cadena, donde uno es un carácter de
        palabra \\w y el otro no.
    -   Al final de la cadena, si el último carácter de la cadena es un
        carácter de palabra \\w.

## Operadores especial

-   **\\n** nueva linea.
-   **\\t** Seleciona tabs.
-   **\\r** Normalmente se usa en combinacion con *\\n* y denota una
    nueva linea. Ejem *'some text\\r\\n'*.

</div>

<div class="cell code" id="vn0_KG1Wiob9">

``` python
import regex as re
import pandas as pd
```

</div>

<div class="cell markdown" id="WcCuj7n5ppJA">

# **Buscando palabras**

Dado el siguiente texto selecciones las palabras bananas y manzanas:

-   *'La manzana es roja, la banana es amarilla, y el limón es verde.'*

</div>

<div class="cell markdown" id="IN0f7L-omTFr">

**esta es una instruccion**

</div>

<div class="cell markdown" id="e-To6XRJrEdP">

## Paso 1:

-   importe la libreria regex.
-   Amacene el texto anterior en una variable.

</div>

<div class="cell code" id="EbEb1e8aqggq">

``` python
import regex as re
texto='La manzana es roja, la banana es amarilla, y el limón es verde.'
```

</div>

<div class="cell markdown" id="yEegg22brX47">

## Paso 2:

-   Cree un patron de busqueda toman en consideracion la funcion de cada
    operador

</div>

<div class="cell code"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}"
id="sLBPPTpbrlvi" outputId="c62786ca-26ff-46a3-efe5-e59cffb6dff1">

``` python
# declare un variable para almacenar el patron de busqueda
patron_de_busqueda= re.compile(r'\b[r,b,m,a,v]\w+\b')
# realice la busqueda del patron dentro del texto
lista_de_resultados=patron_de_busqueda.findall(texto)
print(lista_de_resultados)
```

<div class="output stream stdout">

    ['manzana', 'roja', 'banana', 'amarilla', 'verde']

</div>

</div>

<div class="cell markdown" id="dk75Ov-EtXb7">

### identificar interfaces de un router:

``` bash
Python360YT#show running-config | include hostname
hostname Python360YT
Python360YT#show ip in bri
Python360YT#show ip in brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.48     YES NVRAM  up                    up
GigabitEthernet2       192.168.10.4    YES manual up                    up
GigabitEthernet3       unassigned      YES NVRAM  administratively down down
Loopback0              10.0.0.1        YES NVRAM  up                    up
Loopback1              172.1.1.1       YES manual up                    up
Loopback10             unassigned      YES unset  up                    up
Loopback20             172.168.1.1     YES manual up                    up
Loopback21             172.168.10.1    YES manual up                    up
Loopback42             2.3.3.6         YES other  up                    up
Loopback56             56.56.56.56     YES manual up                    up
Loopback98             172.16.98.1     YES manual up                    up
Loopback99             172.16.1.1      YES manual up                    up
VirtualPortGroup0      192.168.1.1     YES NVRAM  up                    up
Vlan10                 192.168.110.2   YES manual down                  down
Vlan20                 192.168.120.1   YES manual down                  down
Vlan30                 192.168.130.1   YES manual down                  down
Python360YT#
```

``` bash
Python361YT#show running-config | include hostname
hostname Python360YT
Python361YT#show ip in bri
Python361YT#show ip in brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.48     YES NVRAM  up                    up
GigabitEthernet2       unassigned      YES manual administratively down down
GigabitEthernet3       192.168.10.4    YES NVRAM  up                    up
Loopback0              10.0.0.1        YES NVRAM  up                    up
Loopback1              172.1.1.1       YES manual up                    up
Loopback10             unassigned      YES unset  up                    up
Loopback20             172.168.1.1     YES manual up                    up
Loopback21             172.168.10.1    YES manual up                    up
Loopback42             2.3.3.6         YES other  up                    up
Loopback56             56.56.56.56     YES manual up                    up
Loopback98             172.16.98.1     YES manual up                    up
Loopback99             172.16.1.1      YES manual up                    up
VirtualPortGroup0      192.168.1.1     YES NVRAM  up                    up
Vlan10                 192.168.110.2   YES manual down                  down
Vlan20                 192.168.120.1   YES manual down                  down
Vlan30                 192.168.130.1   YES manual down                  down
Python361YT#
```

</div>

<div class="cell code" id="DwD77ZZcySSS">

``` python
r1='''Python360YT#show running-config | include hostname
hostname Python360YT
Python360YT#show ip in bri
Python360YT#show ip in brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.48     YES NVRAM  up                    up
GigabitEthernet2       192.168.10.4    YES manual up                    up
GigabitEthernet3       unassigned      YES NVRAM  administratively down down
Loopback0              10.0.0.1        YES NVRAM  up                    up
Loopback1              172.1.1.1       YES manual up                    up
Loopback10             unassigned      YES unset  up                    up
Loopback20             172.168.1.1     YES manual up                    up
Loopback21             172.168.10.1    YES manual up                    up
Loopback42             2.3.3.6         YES other  up                    up
Loopback56             56.56.56.56     YES manual up                    up
Loopback98             172.16.98.1     YES manual up                    up
Loopback99             172.16.1.1      YES manual up                    up
VirtualPortGroup0      192.168.1.1     YES NVRAM  up                    up
Vlan10                 192.168.110.2   YES manual down                  down
Vlan20                 192.168.120.1   YES manual down                  down
Vlan30                 192.168.130.1   YES manual down                  down
Python360YT#'''
r2='''Python361YT#show running-config | include hostname
hostname Python361YT
Python361YT#show ip in bri
Python361YT#show ip in brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.48     YES NVRAM  up                    up
GigabitEthernet2       unassigned      YES manual administratively down down
GigabitEthernet3       192.168.10.4    YES NVRAM  up                    up
Loopback0              10.0.0.1        YES NVRAM  up                    up
Loopback1              172.1.1.1       YES manual up                    up
Loopback10             unassigned      YES unset  up                    up
Loopback20             172.168.1.1     YES manual up                    up
Loopback21             172.168.10.1    YES manual up                    up
Loopback42             2.3.3.6         YES other  up                    up
Loopback56             56.56.56.56     YES manual up                    up
Loopback98             172.16.98.1     YES manual up                    up
Loopback99             172.16.1.1      YES manual up                    up
VirtualPortGroup0      192.168.1.1     YES NVRAM  up                    up
Vlan10                 192.168.110.2   YES manual down                  down
Vlan20                 192.168.120.1   YES manual down                  down
Vlan30                 192.168.130.1   YES manual down                  down
Python361YT#'''
```

</div>

<div class="cell markdown" id="WIWm3Jd-zYYW">

## Obtener nombre de los routers

itere entre ambas variables y obtenga el nombre de cada router

para obtener el nombre considere la siguiente lista de operadore:

-   **\\b**
-   **\[ \]**
-   **\\w**
-   **+**

cree un patron para identificar los nombre de cada equipo y cree una
lista

</div>

<div class="cell markdown" id="piDwailX101n">

Defina el patron de busqueda

</div>

<div class="cell code" id="DGmdBrj914cN">

``` python
patron=re.compile(r'\bPython\w+\b')
```

</div>

<div class="cell markdown" id="h2s5xn0V1WQD">

forma extendida

</div>

<div class="cell code"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}"
id="BZlZL5aW0TrK" outputId="bf9c609d-3d16-4fd2-ce4b-24f17213132a">

``` python
lista_de_equipos=[]
for item in (r1,r2):
  nombre=patron.findall(item)
  lista_de_equipos.append(nombre)
print([list(set(x))[0] for x in lista_de_equipos])
```

<div class="output stream stdout">

    ['Python360YT', 'Python361YT']

</div>

</div>

<div class="cell markdown" id="5W7vmkaP1qzd">

forma comprimida

</div>

<div class="cell code"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}"
id="GWII2HRSyn6v" outputId="60975138-4bf0-4791-97fd-1cdaa6bd6a65">

``` python
lista_de_equipos=[]
for item in (r1,r2):
  lista_de_equipos.append(patron.findall(item))
print([list(set(x))[0] for x in lista_de_equipos])
```

<div class="output stream stdout">

    ['Python360YT', 'Python361YT']

</div>

</div>

<div class="cell markdown" id="z-ZTrzQZ180t">

List comprehenssion:

</div>

<div class="cell code" id="EikqxnLh2Ati">

``` python
lista_de_equipos=[ list(set(patron.findall(item)))[0] if patron.findall(item) else '' for item in (r1,r2)]
```

</div>

<div class="cell markdown" id="Lrmwhzso2evg">

Verifique el valor de la variable lista_de_equipos

</div>

<div class="cell code"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}"
id="4DNJ4HJn2Kyy" outputId="727c4f78-8c13-47d8-e603-360b5274ed66">

``` python
lista_de_equipos
```

<div class="output execute_result" execution_count="68">

    ['Python360YT', 'Python361YT']

</div>

</div>

<div class="cell markdown" id="lNXSV1I1yAx1">

## Crear un patron de busqueda para interfaces y direcciones ip

-   cree un patron de busqueda que le permite identificar hostname,
    interfaz y direcccion ip
-   Tome el output y seperalo por lineas.
-   cree un diccionario con los resultado
-   cree un dataframe con ese diccionario
-   finalmente escriba el dataframe a un archivo csv

</div>

<div class="cell code" id="-t2W4GAcyNi_">

``` python
reporte={
         'Host Name':[],
         'Interface Id':[],
         'Ip Address':[]}


interfaces_ip=re.compile(r'(\S+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|unassigned)')
for item in (r1,r2):
           #split items by lines
  for x in item.splitlines():
    data=interfaces_ip.findall(x)
    if data:
      reporte['Host Name'].append(list(set(patron.findall(item)))[0])
      reporte['Interface Id'].append(data[0][0])
      reporte['Ip Address'].append(data[0][1])

```

</div>

<div class="cell code" id="3XO34oerzPyD">

``` python
Data_reporte = pd.DataFrame(reporte)
```

</div>

<div class="cell code"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:1000}"
id="H9FfTJy60eC_" outputId="32cb0f85-e68f-4cd3-81a1-1aaf08f4a880">

``` python
Data_reporte
```

<div class="output execute_result" execution_count="93">

``` json
{"summary":"{\n  \"name\": \"Data_reporte\",\n  \"rows\": 32,\n  \"fields\": [\n    {\n      \"column\": \"Host Name\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Python361YT\",\n          \"Python360YT\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Interface Id\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 16,\n        \"samples\": [\n          \"GigabitEthernet1\",\n          \"GigabitEthernet2\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Ip Address\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 15,\n        \"samples\": [\n          \"172.16.98.1\",\n          \"192.168.1.1\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"Data_reporte"}
```

</div>

</div>

<div class="cell code" id="xDW68Tr46wCf">

``` python
```

</div>
