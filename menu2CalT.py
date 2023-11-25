import os
import json

import funcionCalificar
def menu2CalT ():
    contCalT = True        
    while (contCalT == True):
        print("\n\n############## Cinema+:                ##############")
        print("######         Calificacion de titulos         ######")
        print("#                                                   #")
        print("#      [1] Calificacion de titulos                  #")
        print("#                                                   #")
        print("#                                                   #")
        print("#      [0] Volver                                   #")
        print("#                                                   #")
        print("#####################################################")
        opcionCalT = input("\nIngrese una opcion: ")
        if(opcionCalT == '1'):
            archivo = open("peliculas.json","r")
            peliculas = json.load(archivo)
            archivo.close()
            funcionCalificar.calificar_pelicula(peliculas)
             
        elif(opcionCalT == '0'):
            os.system("cls")
            contCalT = False
                