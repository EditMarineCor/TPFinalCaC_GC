import os

def menu3ListEst():
    contLE = True
    while (contLE == True):
        print("\n\n############## Cinema+:                ##############")
        print("############# Reportes y estadisticas  ##############")
        print("#                                                   #")
        print("#      [1] Listado de Peliculas                     #")
        print("#      [2] Peliculas de mayor puntaje               #")
        print("#      [3] Peliculas disponibles en la plataforma   #")
        print("#      [0] Volver                                   #")
        print("#                                                   #")
        print("#####################################################")
        
        opcionLE = input("\nIngrese una opcion: ")
        if(opcionLE == '1'):
            os.system("cls")
            print("\n\n#####################################################")
            print("#                                                   #")
            print("#      [1] Listado de Peliculas                     #")
            print("#                                                   #")
            print("#####################################################")
            
            def list_pelis():
                print("Aqui va la funcion listado de peliculas")
        
        elif(opcionLE == '2'):
            os.system("cls")
            print("\n\n#####################################################")
            print("#                                                   #")
            print("#      [2] Peliculas de mayor puntaje               #")
            print("#                                                   #")
            print("#####################################################")
            
            def mayor_punt():
                print("Aqui va la funcion mayor puntaje")
                
        elif(opcionLE == '3'):
            os.system("cls")
            print("\n\n#####################################################")
            print("#                                                   #")
            print("#      [3] Peliculas disponibles en la plataforma   #")
            print("#                                                   #")
            print("#####################################################")
            
            def disp_plataforma():
                print("Aqui va la funcion disponibles es plataforma")
                
        elif(opcionLE == '0'):
            os.system("cls")
            print("\n\n#####################################################")
            print("#                                                   #")
            print("#      [0] Volver                                   #")
            print("#                                                   #")
            print("#####################################################")
            
            def volver():
                print("Aqui volver al MP")
            contLE = False
                
