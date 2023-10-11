import pandas as pd

"""Definición de fuentes"""
alquiler_distritos_madrid_dataset = "W:/document/Programación Python/Parte 1/Tema 2/alquiler-madrid-distritos.csv"
alquiler_pisos_municipios_dataset = "W:/document/Programación Python/Parte 1/Tema 2/alquiler-madrid-municipios.csv"



alquiler_pisos_municipios = pd.read_csv(alquiler_distritos_madrid_dataset, sep=",", index_col=False)
alquiler_distritos_madrid = pd.read_csv(alquiler_pisos_municipios_dataset, sep=",", index_col=False)

alquiler_pisos_municipios.columns
alquiler = alquiler_pisos_municipios

alquiler.dtypes

#### describir el index
alquiler.index
# cambiar el index
alquiler_nuevo_indice = alquiler.set_index(['distrito', 'anyo', 'cuatrimestre'])
alquiler_nuevo_indice.head()

alquiler.tail()

alquiler['distrito','precio']
alquiler_nuevo_indice.shape

############################

alquiler.iloc[200] # seleccionar la  fila que  tiene el indice 200

alquiler.iloc[3:5] # seleccionar de l fila 3 a la fila 5-1

alquiler.iloc[3:5, 1:] #alquiler.iloc[3:5, :2 o 0:3 la prima  columna inicia por 0 es  decir  la  columna distrito]# seleccionar de l fila 3 a la fila 5-1  y  de la columna 1  hasta el final -1


alquiler.iloc[[1,2,4],[0,3]]

alquiler.iloc[-3:-1] #filas y columnas pero inicias a  contar desde la ultima  fila y columna

######loc para  valores categoricos

alquiler_nuevo_indice.loc[('Centro', 2014, 2)] 
alquiler_nuevo_indice.loc[('Centro', 2010)]

########condiciones para seleccionar valores

alquiler[alquiler.distrito == 'Retiro'].head() #alquiler.distrito  e sigual a alquiler['distrito']

alquiler[(alquiler.distrito == 'Retiro') & (alquiler.anyo >= 2012) & (alquiler.anyo <= 2016)]

alquiler[(alquiler.distrito == 'Retiro') & ((alquiler.anyo == 2012) | (alquiler.anyo == 2016))]


alquiler[(alquiler.distrito == 'Retiro') & (alquiler.anyo == 2012)]['precio']

#### ordenación

alquiler.sort_values(['distrito'], ascending=True) # una  columna

alquiler.sort_values(['distrito', 'anyo', 'cuatrimestre'], ascending=[True, True, False]) # varias  columna
###########
alquiler_2 = alquiler.copy()
alquiler_2['precio_90m'] = alquiler_2.precio * 90

###########renombrar

alquiler_2 = alquiler_2.rename(columns={'precio_90m' : ' precio_90_metros'})


############object = texto o  string

##################
