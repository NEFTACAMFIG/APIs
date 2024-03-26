#Se crea la base de datos en donde guardaremos las tablas de información
conn = sqlite3.connect('Project_Music.db')
cursor = conn.cursor();

#Se crean las tablas de la base de datos tanto para los datos de México como para los datos globales
cursor.execute("""CREATE TABLE 
  spotifyMEX(
    popularity int, 
    name text, 
    PRIMARY KEY (name)
  )
  """)

cursor.execute("""CREATE TABLE 
  deezerMEX(
    rank int, 
    name text, 
    PRIMARY KEY (name)
  )
  """)

cursor.execute("""CREATE TABLE 
  youtubeMEX(
    likecount int, 
    name text, 
    PRIMARY KEY (name)
  )
  """)

cursor.execute("""CREATE TABLE 
  spotifyG(
    popularityG int, 
    name text, 
    PRIMARY KEY (name)
  )
  """)

cursor.execute("""CREATE TABLE 
  deezerG(
    rankD int, 
    name text, 
    PRIMARY KEY (name)
  )
  """)

cursor.execute("""CREATE TABLE 
  youtubeG(
    likecountY int, 
    name text, 
    PRIMARY KEY (name)
  )
  """)

#Este cofigo sirve para crear tablas de forma independiente en caso de equivocarse en el codigo de arriba
#cursor.execute("""CREATE TABLE 
 # deezerMEX(
  #  rank int, 
   # name text, 
    #PRIMARY KEY (name)
  #)
  #""")

#Comprobación de que existen las tablas
tabla_de_sqlite3 = cursor.execute("""SELECT * FROM sqlite_master WHERE type='table'""")

for tupla in tabla_de_sqlite3:
  print(tupla)

#En caso de que se tenga que borrar una tabla se puede usar este código
#cursor.execute("DROP TABLE deezerG")
