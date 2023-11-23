import json
import os
dirDeTrabajo = os.path.dirname(__file__)
os.chdir(dirDeTrabajo)


archivo = open("peliculas.json","r")
peliculas = json.load(archivo)

def mostrar_listado_peliculas():
    print("Listado de películas:")
    peliculas.sort(key=lambda x: x['titulo'])
    for pelicula in peliculas:
        print(f"{pelicula['titulo']} - {pelicula['genero']} - Calificacion: {pelicula['calificacion']}")




def peliculas_mayor_puntaje():
    for pelicula in peliculas: # Aqui calcula el promedio de las calificaciones de la lista
      pelicula['calificacion'] = sum(pelicula['calificacion'])/len(pelicula)
    
    peliculas.sort(key=lambda x: x['calificacion'], reverse=True)
    for pelicula in peliculas[0:15]: # Imprimimos las primeras 15 peliculas
      print(f"Titulo: {pelicula.get('titulo', 'N/A')}, Genero: {pelicula.get('genero', 'N/A')}, Calificación: {pelicula.get('calificacion', 'N/A')}")
      print() # Espacio vacio

def mostrar_peliculas_disponibles():
    
    for pelicula in peliculas:
        try:
            if pelicula['disponible'] == True :
                print(f"Titulo: {pelicula['titulo']} - Disponible")
        except: 
            print("\n")

while True:  
   print("CINEMA+")
   print("Reportes y estadísticas")
   print("1 - Listado de películas")
   print("2 - Películas de mayor puntaje")
   print("3 - Películas disponibles en la plataforma")
   print("0 - Volver")
  
   opcion_5=int(input("Ingrese la opcion que quieras realizar: "))
   if opcion_5 == 1: 
     
     mostrar_listado_peliculas()
   elif opcion_5 == 2: 
     print("Películas de mayor puntaje ") 
     peliculas_mayor_puntaje()
   elif opcion_5 == 3:  
     print("Películas disponibles en la plataforma") 
     mostrar_peliculas_disponibles()
   elif opcion_5 == 0:
            if input("¿Estás seguro de que quieres salir? (s/n): ").lower() == "s":
             break
   else:
     print("La opción no es valida ,elija una correcta!")    

archivo.close()