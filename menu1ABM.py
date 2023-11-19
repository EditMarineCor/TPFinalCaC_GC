import os
import funcAlta
import funcModif
import funcBaja

def menu1ABM ():
    contABM = True # Continuar ABM      
    while (contABM == True):
        print("\n\n############## Cinema+:                ##############")
        print("###### Alta, Baja y Modificacion de peliculas  ######")
        print("#                                                   #")
        print("#      [1] Alta de nueva pelicula                   #")
        print("#      [2] Modificacion de pelicula existente       #")
        print("#      [3] Baja de pelicula (eliminar)              #")
        print("#      [0] Volver                                   #")
        print("#                                                   #")
        print("#####################################################")
        opcionABM = input("\nIngrese una opcion: ")
        if(opcionABM == '1'):
            os.system("cls")
            print("\n\n#####################################################")
            print("#                                                   #")
            print("#      [1] Alta de nueva pelicula                   #")
            print("#                                                   #")
            print("#####################################################")
            
            funcAlta.alta_peli()
        
        elif(opcionABM == '2'):
            os.system("cls")
            print("\n\n#####################################################")
            print("#                                                   #")
            print("#      [2] Modificacion de pelicula existente       #")
            print("#                                                   #")
            print("#####################################################")
            
            funcModif.modif_peli()
                
        elif(opcionABM == '3'):
            os.system("cls")
            print("\n\n#####################################################")
            print("#                                                   #")
            print("#      [3] Baja de pelicula (eliminar)              #")
            print("#                                                   #")
            print("#####################################################")
            
            funcBaja.baja_peli()
                
        elif(opcionABM == '0'):
            os.system("cls")
            print("\n\n#####################################################")
            print("#                                                   #")
            print("#      [0] Volver                                   #")
            print("#                                                   #")
            print("#####################################################")
            
            contABM = False
                