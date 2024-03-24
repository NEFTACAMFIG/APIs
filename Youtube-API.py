import json
import requests

#Extraccion de datos de la API de YOUTUBE. Las 100 canciones mas populares México
api_key = 'Your_API_here'

youtube = build('youtube', 'v3', developerKey=api_key)

playlist_id = 'PL4fGSI1pDJn6fko1AmNa_pdGPZr5ROFvd'
#playlist_id2 = 'PL4fGSI1pDJn5kI81J1fYWK5eZRl1zJ5kM'

videos = []
ratings = []
todos = []

nextPageToken = None
while True:
    pl_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlist_id,
        maxResults=50,
        pageToken=nextPageToken
    )

    pl_response = pl_request.execute()

    vid_ids = []
    for item in pl_response['items']:
        vid_ids.append(item['contentDetails']['videoId'])

    vid_request = youtube.videos().list(
        part="snippet",
        id=','.join(vid_ids)
    )

    vid_response = vid_request.execute()

    vid_request2 = youtube.videos().list(
        part="statistics",
        id=','.join(vid_ids)
    )

    vid_response2 = vid_request2.execute()

    for item in vid_response['items']:
        vid_views = item['snippet']['title']

        videos.append(vid_views)

    for item in vid_response2['items']:
        vid_rating = item['statistics']['likeCount']

        ratings.append(vid_rating)

    nextPageToken = pl_response.get('nextPageToken')

    if not nextPageToken:
        break

#videos.sort(key=lambda vid: vid['views'], reverse=True)
i = 0
for video in videos:
    todos.append([int(ratings[i]),video])
    i = i + 1
todos.sort(reverse = True)
print(todos)

#Comenzamos con la limpieza de datos eliminando la primera parte del string, la cual contiene al autor de la canción
# Sin embargo nosotros relacionaremos el titulo de cancion por lo que esta es la informacion que necesitamos
o = 0
for j in todos:
  if '-' in j[1]:
    z = j[1].find('-')
    y = j[1][z+2:]
    #print(j[1],y)
    todos[o][1]=todos[o][1].replace(j[1],y)
    
    o = o + 1
  else:
    o = o + 1
print(todos)

#Esta parte del codigo corresponde a eliminar la parte del string que contiene la cadena 'Official Video'
o = 0
for j in todos:
  if '(' in j[1]:
    z = j[1].find('(')
    z = z-1
    y = j[1][0:z]
    #print(len(y))
    todos[o][1]=todos[o][1].replace(j[1],y)
    todos[o][1] = todos[o][1].rstrip()
    o = o + 1

  elif '[' in j[1]:
    z = j[1].find('[')
    z = z-1
    y = j[1][0:z]
    #print(y)
    todos[o][1]=todos[o][1].replace(j[1],y)
    todos[o][1] = todos[o][1].rstrip()
    o = o + 1

  else:
    o = o + 1
print(todos)

#Extraccion de datos de la API de YOUTUBE. Las 100 canciones mas populares nivel mundial
api_key = 'Your_API_here'

youtube = build('youtube', 'v3', developerKey=api_key)

playlist_id = 'PL4fGSI1pDJn6puJdseH2Rt9sMvt9E2M4i'

videos_global = []
ratings_global = []
todos_global = []

nextPageToken = None
while True:
    pl_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlist_id,
        maxResults=50,
        pageToken=nextPageToken
    )

    pl_response = pl_request.execute()

    vid_ids = []
    for item in pl_response['items']:
        vid_ids.append(item['contentDetails']['videoId'])

    vid_request = youtube.videos().list(
        part="snippet",
        id=','.join(vid_ids)
    )

    vid_response = vid_request.execute()

    vid_request2 = youtube.videos().list(
        part="statistics",
        id=','.join(vid_ids)
    )

    vid_response2 = vid_request2.execute()

    for item in vid_response['items']:
        vid_views = item['snippet']['title']

        videos_global.append(vid_views)

    for item in vid_response2['items']:
        vid_rating = item['statistics']['likeCount']

        ratings_global.append(vid_rating)

    nextPageToken = pl_response.get('nextPageToken')

    if not nextPageToken:
        break

#videos.sort(key=lambda vid: vid['views'], reverse=True)
i = 0
for video in videos:
    todos_global.append([int(ratings[i]),video])
    i = i + 1
todos_global.sort(reverse=True)
print(todos_global)

#Comenzamos con la limpieza de datos eliminando la primera parte del string, la cual contiene al autor de la canción
# Sin embargo nosotros relacionaremos el titulo de cancion por lo que esta es la informacion que necesitamos
o = 0
for j in todos_global:
  if '-' in j[1]:
    z = j[1].find('-')
    y = j[1][z+2:]
    #print(j[1],y)
    todos_global[o][1]=todos_global[o][1].replace(j[1],y)
    o = o + 1
  else:
    o = o + 1

#Esta parte del codigo corresponde a eliminar la parte del string que contiene la cadena 'Official Video'
o = 0
for j in todos_global:
  if '(' in j[1]:
    z = j[1].find('(')
    z = z-1
    y = j[1][0:z]
    todos_global[o][1]=todos_global[o][1].replace(j[1],y)
    o = o + 1

  elif '[' in j[1]:
    z = j[1].find('[')
    z = z-1
    y = j[1][0:z]
    todos_global[o][1]=todos_global[o][1].replace(j[1],y)
    o = o + 1

  else:
    o = o + 1
print(todos_global)
