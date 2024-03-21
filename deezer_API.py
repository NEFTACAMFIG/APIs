pip install deezer-python

import json
import requests
import deezer

#Extraccion de datos de la API de Deezer. Las 100 canciones mas populares en México
query = 'album:"Ich schwanke noch" artist:"Ikke Hüftgold"'
responsed = requests.get(
    'https://api.deezer.com/playlist/1111142361'
)
#print(response)
response_jsond = responsed.json()
#print(response_jsond)

#Los datos obtenidos de Deezer se pasan a una lista para posteriormente crear la base de datos en SQL
d = []
for q in response_jsond["tracks"]["data"]:
  d.append([q["rank"],q["title"]])
#print(d)

#Se ordenan los datos antes de pasarlos a una base de datos
d.sort(reverse = True)
print(d)

#Extraccion de datos de la API de Deezer. Las 100 canciones mas populares a nivel mundial
query = 'album:"Ich schwanke noch" artist:"Ikke Hüftgold"'
responsed_global = requests.get(
    'https://api.deezer.com/playlist/3155776842'
)
#print(response)
response_jsond_global = responsed_global.json()
#print(response_jsond)

#Los datos obtenidos de Deezer se pasan a una lista para posteriormente crear la base de datos en SQL
d_global = []
for q in response_jsond_global["tracks"]["data"]:
  d_global.append([q["rank"],q["title"]])
#print(d)

#Se ordenan los datos antes de pasarlos a una base de datos
d_global.sort(reverse = True)
print(d_global)

d_global[37][1]=d_global[37][1].replace("Beggin'","Beggin")
print(d_global[37][1])
