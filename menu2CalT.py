import os

def menu2CalT ():
    contCalT = True        
    while (contCalT == True):
        print("\n\n############## Cinema+:                ##############")
        print("###### Alta, Baja y Modificacion de peliculas  ######")
        print("#                                                   #")
        print("#      [1] Calificacion de titulos                  #")
        print("#      [2] Mostrar datos de calificacion            #")
        print("#      [3]                                          #")
        print("#      [0]                                          #")
        print("#                                                   #")
        print("#####################################################")
        opcionCalT = input("\nIngrese una opcion: ")
        if(opcionCalT == '1'):
            os.system("cls")
            print("\n\n#####################################################")
            print("#                                                   #")
            print("#      [1] funcion de calificacion1                 #")
            print("#                                                   #")
            print("#####################################################")
            
            def calif_pelis():
                print("Aqui va la funcion random que genera los titulos")
        
        elif(opcionCalT == '2'):
            os.system("cls")
            print("\n\n#####################################################")
            print("#                                                   #")
            print("#      [2] funcion de calificacion2                 #")
            print("#                                                   #")
            print("#####################################################")

            def mostrar_calif():
                print("Aqui va Mostrar datos de calificacion")
            
        elif(opcionCalT == '0'):
            os.system("cls")
            print("\n\n#####################################################")
            print("#                                                   #")
            print("#      [0] Volver                                   #")
            print("#                                                   #")
            print("#####################################################")
            
            def volver():
                print("Aqui volver al MP")
            contCalT = False
                