import pandas as pd
clientes={
    #Llave   List inician en 0   
    'Nombre':['Juan','Maria','Pedro','Ana'],
    'Edad':[25,30,35,40],
    'Ciudad':['Madrid','Barcelona','Sevilla','Valencia']
}
#print(f'Nombre {clientes["Nombre"][0]}')
#print('Nombre {} edad {}  Ciudad {}'.format(clientes["Nombre"][0],clientes["Edad"][0],clientes["Ciudad"][0]))
df =pd.DataFrame(clientes)
print('\n')
print(df)
