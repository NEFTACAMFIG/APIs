import plotly.express as px

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

#Este código sirva para cambiar el numero de datos que se muestran cuando mandas a llamar el Dataframe
#pd.set_option('max_rows', 100)

#Se utiliza este código para hacer una última etapa de limpieza en donde se verifica que los datos correspondan con la información vista en las APIS
#df4 = df4.replace("Sweet Child O Mine","Sweet Child O' Mine")

#Se cambian los nombres de las canciones a mayusculas para homogenizar estos datos y se puedan relacionar entre ellos
df1['name'] = df1['name'].str.upper()
df2['name'] = df2['name'].str.upper()
df3['name'] = df3['name'].str.upper()
df4['name'] = df4['name'].str.upper()
df5['name'] = df5['name'].str.upper()
df6['name'] = df6['name'].str.upper()

#Este código sirve para exportar los Dataframes creados a archivos .CSV. Esto sirve para no correr todo el código de nuevo en posteriores consultas
#df1.to_csv('df1.csv')
#df2.to_csv('df2.csv')
#df3.to_csv('df3.csv')
#df4.to_csv('df4.csv')
#df5.to_csv('df5.csv')
#df6.to_csv('df6.csv')

conn.commit()
conn.close()

#Para cargar los datos 
#df1 = pd.read_csv('/content/drive/MyDrive/Mis Documentos/Curso de Python/PROYECTOS/Proyecto APIS y Data Wrangling/df1.csv')

#df1 = df1.drop(['Unnamed: 0'],axis=1)

#Este codigo sirve para acomodar las columnas del Datframe como a nosotros nos ayude mejor
df1 = df1[['name','popularity']]
df2 = df2[['name','popularityG']]
df3 = df3[['name','rank']]
df4 = df4[['name','rankD']]
df5 = df5[['name','likecount']]
df6 = df6[['name','likecountY']]

#Este codigo se utiliza en caso de tener que cambiar el nombre de las columnas de nuestro dataframe
#df2 = df2.rename(columns={'nameG':'name'})

# 6. Unión de datos para compararlos, encontrar coincidencias y correlaciones

#Se unen los datos para las canciones MAS POPULARES DE MEXICO en tres plataformas diferentes
dtMEX1 = pd.merge(df1,df3)
dtMEX2 = pd.merge(dtMEX1,df5)

#Se guarda la información de las canciones mas populares de Mexico en tres plataformas diferentes
dtMEX2
dtMEX2.to_csv('dtMEX2.csv')

#Se unen los datos para las canciones MAS POPULARES A NIVEL GLOBAL en tres plataformas diferentes
dtG1 = pd.merge(df2,df4)
dtG2 = pd.merge(dtG1,df6)

#Se guarda la información de las canciones mas populares a NIVEL GLOBAL en tres plataformas diferentes
dtG2
dtG2.to_csv('dtG2.csv')

# 7. Visualización de resultados

# Canciones más populares a nivel Mundial( Septiembre 2022)
fig = px.scatter_3d(dtG2, x='popularityG', y = 'rankD', z = 'likecountY',
      color = 'name', size = 'likecountY' )
fig.show()

# Canciones más populares en México (Septiembre 2022)
fig = px.scatter_3d(dtMEX2, x='popularity', y = 'rank', z = 'likecount',
      color = 'name', size = 'likecount' )
fig.show()
