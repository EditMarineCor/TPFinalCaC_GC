import os
# import funcModif

def menu4Busq():
    contModif = True
    while (contModif == True):
        print("#                                                   #")
        print("#      [1] Buscar por id                            #")
        print("#      [2] Buscar por titulo                        #")
        print("#      [3] Busqueda secuencial (si no sabe el id)   #")
        print("#      [0] Volver                                   #")
        print("#                                                   #")
        print("#####################################################")
        opcionBusq = input("\nIngrese una opcion: ")
        if(opcionBusq == "1"):
            os.system("cls")
            print("\n\n#####################################################")
            print("#                                                   #")
            print("#      [1] Busqueda por id                          #")
            print("#                                                   #")
            print("#####################################################")
            buscado = int(input("Ingrese el id (numero entero): "))
            return (opcionBusq, buscado)

        elif(opcionBusq == "2"):
            os.system("cls")
            print("\n\n#####################################################")
            print("#                                                   #")
            print("#      [2] Busqueda por titulo                      #")
            print("#                                                   #")
            print("#####################################################")
            buscado = input("Ingrese el titulo o parte de el: ")
            return (opcionBusq, buscado)

        elif(opcionBusq == "3"):
            os.system("cls")
            print("\n\n#####################################################")
            print("#                                                   #")
            print("#      [3] Busqueda secuencia                       #")
            print("#                                                   #")
            print("#####################################################")
            buscado = "todos"
            return (opcionBusq, buscado)

        elif(opcionBusq == "0"):
            os.system("cls")
            print("\n\n#####################################################")
            print("#                                                   #")
            print("#      [0] Volver                                   #")
            print("#                                                   #")
            print("#####################################################")
            buscado = "salir"
            return (opcionBusq, buscado)