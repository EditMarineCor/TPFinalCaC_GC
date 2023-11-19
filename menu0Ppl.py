import os
import menu1ABM
import menu2CalT
import menu3ListEst

def menu0Ppl():
    contMP = True
    while (contMP == True):
        os.system("cls")
        print("\n\n############## Cinema+: Menu Principal ##############")
        print("#                                                   #")
        print("#      [1] ABM de peliculas                         #")
        print("#      [2] Calificacion de titulos                  #")
        print("#      [3] Reportes y estadisticas                  #")
        print("#      [0] Salir del programa                       #")
        print("#                                                   #")
        print("#####################################################")
        
        opcionP = input("\nIngrese una opcion: ")
        
        if(opcionP == "1"):
            os.system("cls")
            menu1ABM.menu1ABM()
        
        elif(opcionP == "2"):
            os.system("cls")
            menu2CalT.menu2CalT()
        
        elif(opcionP == "3"):
            os.system("cls")
            menu3ListEst.menu3ListEst()
            
        elif(opcionP == "0"):
            os.system("cls")
            print("\n\n############## Cinema+:                ##############")
            print("############# Calificacion de Titulos  ##############")
            print("#                                                   #")
            print("#          SALIENDO DEL PROGRAMA  CINEMA+           #")
            print("#                                                   #")
            print("#####################################################")
            contMP = False
