import json
import os
try:
     with open ('peliculas.json','r')as archivo:#cargar peliculas desde el archivo
          peliculas=json. load(archivo)
          for pelicula in peliculas:
             if "calificacion" not in pelicula:
                pelicula["calificacion"]=[]
except FileNotFoundError:
    print("No se encontro el archivo 'peliculas.json'. asegurate de que exista y tenga peiculas a calificar.")
    exit()
print("#"*90)
print("#                                                                                        #")
print("#  CINEMA+ #"*7)
print("#                                                                                        #")
print("#"*90)
while True:   
 print("#"*90)
 print("#                                                                                        #")       
 print("#                                REPORTES Y ESTADISTICAS                                 #")
 print("#                                                                                        #")       
 print("#"*90)
 print(f"""       
                  # 1-Lstados de Peliculas: Titulo,Genero y Calificacion
                  # 2-Peliculas de Mayor Puntaje
                  # 3-peliculas Disponibles en la Plataforma
                  # 0- Volver
              
              """)
 print("#"*90)
 opcion_reportes=int(input("Ingresa una opcion: "))
 os.system("cls")
 if opcion_reportes==1:
          print("#"*90)
          print("#                                                                                        #")
          print("#  CINEMA+ #"*7)
          print("#                                                                                        #")
          print("#"*90)
          print("#"*90)
          print("# Listado de Peliculas: Titulo, Genero y Calificacion") 
          print("#"*90)
          print("")
          peliculas_ordenadas=sorted(peliculas,key=lambda x:x.get('titulo',''))#ordenar peliculas por titulo
          for pelicula in peliculas_ordenadas:#mostrar peliculas ordenadas
            titulo=pelicula.get('titulo','Titulo no disponible')
            genero=pelicula.get('genero','Genero no disponible')
            calificacion=pelicula.get('calificacion','Calificacion no disponible')
            print(f"Titulo: {titulo}")
            print(f"Genero:{genero}")
            print(f"Calificacion;{calificacion}") 
            print("-"*90)
          continue
 elif opcion_reportes==2:
     print("#"*90)
     print("#                                                                                        #")
     print("#  CINEMA+ #"*7)
     print("#                                                                                        #")
     print("#"*90)
     print("#"*90)
     print("# Peliculas de Mayor Puntaje") 
     print("#"*90)

     peliculas.sort(key=lambda x:sum(x.get("calificacion",[]))/len(x.get("calificacion")),reverse=True)#calcula la suma de las calificaciones de una pelicula
     print("")
     print("Ranking de las 10 Peliculas con mayor puntaje en la plataforma: ")
     print("#"*90)
     print("")
     for pelicula in peliculas[:10]:
      titulo=pelicula.get("titulo","Titulo no especificado")
      calificacion=sum(pelicula.get("calificacion",[]))
      print("")
      print(f"{titulo}: Calificacion total: {calificacion}")
      print("-"*90)
     continue
 elif opcion_reportes==3:
    print("#"*90)
    print("#                                                                                        #")
    print("#  CINEMA+ #"*7)
    print("#                                                                                        #")
    print("#"*90)
    print("#"*90)
    print("# Peliculas Disponibles en la Plataforma") 
    print("#"*90)
    peliculas_disponibles=[pelicula for pelicula in peliculas if pelicula.get('disponible',False)]#filtra las peliculas disponibles
    for pelicula in peliculas_disponibles:
        titulo=pelicula.get('titulo','titulo no disponible')
        print("")
        print(f"Titulo:{titulo} ")
        print("-"*90)
    continue
 else:
    opcion_reportes==0
    print("Saliendo de Reportes y Estadisticas")
    break
 
  