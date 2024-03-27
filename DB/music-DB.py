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

# Indexing data on the different tables
#Se insertan los datos a la tabla 
for i in range(len(s)):
  z = "INSERT INTO spotifyMEX VALUES (" + str(s[i][0]) + "," + " '" + str(s[i][1]) + ("')")
  cursor.execute(z)

for j in range(len(s_global)):
  y = "INSERT INTO spotifyG VALUES (" + str(s_global[j][0]) + "," + " '" + str(s_global[j][1]) + ("')")
  #print(y)
  cursor.execute(y)

for k in range(len(d)):
  x = "INSERT INTO deezerMEX VALUES (" + str(d[k][0]) + "," + " '" + str(d[k][1]) + ("')")
  cursor.execute(x)

for l in range(len(d_global)):
  w = "INSERT INTO deezerG VALUES (" + str(d_global[l][0]) + "," + " '" + str(d_global[l][1]) + ("')")
  #print(w)
  cursor.execute(w)

for m in range(len(todos)):
  t = "INSERT INTO youtubeMEX VALUES (" + str(todos[m][0]) + "," + " '" + str(todos[m][1]) + ("')")
  cursor.execute(t)

for n in range(len(todos_global)):
  u = "INSERT INTO youtubeG VALUES (" + str(todos_global[n][0]) + "," + " '" + str(todos_global[n][1]) + ("')")
  cursor.execute(u)

#Este codigo sirve para comprobar de que los datos se hayan añadido en las tablas solo que tiene que cambiar el nombre de la tabla
#tabla_usuarios = cursor.execute("SELECT * FROM deezerMEX")

#tabla_usuarios

#for tupla in tabla_usuarios:
 # print(tupla)

#Las tablas creadas se pasan a Dataframes para manipularlos con Pandas
dfS1 = pd.read_sql('SELECT * FROM spotifyMEX',conn)
df1 = pd.DataFrame(dfS1)

dfS2 = pd.read_sql('SELECT * FROM spotifyG',conn)
df2 = pd.DataFrame(dfS2)

dfD1 = pd.read_sql('SELECT * FROM deezerMEX',conn)
df3 = pd.DataFrame(dfD1)

dfD2 = pd.read_sql('SELECT * FROM deezerG',conn)
df4 = pd.DataFrame(dfD2)

dfYT1 = pd.read_sql('SELECT * FROM youtubeMEX',conn)
df5 = pd.DataFrame(dfYT1)

dfYT2 = pd.read_sql('SELECT * FROM youtubeG',conn)
df6 = pd.DataFrame(dfYT2)

# Limpieza de datos con Pandas
