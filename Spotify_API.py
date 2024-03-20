pip install spotipy --upgrade
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
import time
import json
import requests

#Credenciales para poder usar la API de Spotify
client_ID = 'ID'
client_Secret = 'API_KEY'
client_credentials_manager = SpotifyClientCredentials(client_ID,client_Secret)

#Extrayendo datos de las 50 canciones mas populares en México Spotify
query = 'https://api.spotify.com/v1/playlists/37i9dQZEVXbO3qyFxbkOE1/tracks'
token1 = 'Token obteined from the API'
response = requests.get(query,data=None, headers ={
    "Accept":"aplication/json",
    "Content-Type":"aplication/json",
    "Authorization":"Bearer {}".format(token1)
})

response_json = response.json()
#print(response_json)

for p in response_json["items"]:
  print(p["track"]["popularity"],p['track']['name'])

#Los datos recolectados se pasan a una lista
s = []
for q in response_json["items"]:
  s.append([q["track"]["popularity"],q['track']['name']])

#Se ordena la lista
s.sort(reverse = True)
print(s)

#Extrayendo datos de las 50 canciones mas populares a nivel global Spotify
query = 'https://api.spotify.com/v1/playlists/37i9dQZEVXbMDoHDwVN2tF/tracks'
token = 'Token obteined from the API'
response_global = requests.get(query,data=None, headers ={
    "Accept":"aplication/json",
    "Content-Type":"aplication/json",
    "Authorization":"Bearer {}".format(token)
})

response_json2 = response_global.json()
#print(response_json)

for p in response_json2["items"]:
  print(p["track"]["popularity"],p['track']['name'])

#Los datos recolectados se pasan a una lista
s_global = []
for q in response_json2["items"]:
  s_global.append([q["track"]["popularity"],q['track']['name']])

#Se ordena la lista
s_global.sort(reverse = True)
print(s_global)

# Cleaning some data
s_global[12][1]=s_global[12][1].replace("Ain't","Aint")
print(s_global[12][1]
