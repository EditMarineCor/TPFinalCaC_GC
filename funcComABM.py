import json

# Funciones comunes a todas las funciones ABM
def cargar_peliculas():# Carga la BD Json de peliculas
    try: 
        with open("peliculas.json", "r") as archivo:
            return json.load(archivo) 
    except FileNotFoundError: 
        peliculas = []
        guardar_peliculas(peliculas)
        print("El archivo que desea abrir no existe!!")
        
def guardar_peliculas(peliculas): 
    with open("peliculas.json", "w") as archivo: 
        json.dump(peliculas, archivo)

def validar_Gen():
        lista_genero = ["1 - Acción", "2 - Animación", "3 - Comedia", 
                        "4 - Drama", "5 - Ciencia ficción", "6 - Terror",
                        "7 - Suspenso", "8 - Romántica"]
        condicion = True
        while(condicion == True):
            print("\nOpciones de genero: ", lista_genero)
            gen = int(input("Ingresa el genero de la pelicula (1 al 8): "))
            if(0 < gen < 9):
                condicion = False
            else:
                print("\nIngrese una opcion valida!!")
        return lista_genero[gen -1][4::]

def validar_Clasif():
        lista_clasific = ["1 - ATP", "2 - PG", "3 - PG-14", "4 - R", "5 - NC-18"]
        condicion = True
        while(condicion == True):
            print("\nOpciones de clasificacion: ", lista_clasific)
            clasif = int(input("Ingresa la clasificacion de la pelicula (1 al 5): "))
            if(0 < clasif < 6):
                condicion = False
            else:
                print("\nIngrese una opcion valida!!")
        return lista_clasific[clasif -1][4::]