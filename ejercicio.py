import pandas as pd

#Creacion de dataFrames
Parque = {
    'parques' : ['Chicamocha', 'Tayrona', 'Mavecure', 'Chingaza'],
    'Tipo': ['Flora', 'Fauna', 'Flora', 'Fauna'],
    'Especie' : ['Danta', 'Oso Anteojos', 'Aguila Arpia', 'Orquidea Morada'],
    'Riesgo' : ['alto', 'Medio', 'Bajo', 'Medio'],
    'Ejemplares' : [5,8,7,4]

}
indice = ['uno', 'dos', 'tres', 'cuatro']

df = pd.DataFrame(Parque, index= indice)
print(df)

print(df['parques'])
print(df['Especie'])


print(df.iloc[3,3])
print(df.iloc[2,3])
print(df.iloc[3,2])

promdios = df.groupby('parques')['Ejemplares'].mean()
print(promdios)