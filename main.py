import time
import os

time.sleep(1)

My_List = [[], [], [], []]

Eleccion = 0

def Altas():
    while True:
        Dni = input("D.N.I. (Pulse enter para salir )")
        if Dni == "":
            break
        else:
            Nombre = input("Nombre ")
            Primer_Ap = input("Primer Apellido: ")
            Segundo_ap = input("Segundo Apellido ")
            os.system("")
            My_List[0].append(Dni)
            My_List[1].append(Nombre)
            My_List[2].append(Primer_Ap)
            My_List[3].append(Segundo_ap)

def Bajas():
    # print("Número de registros ", My_List)
    # time.sleep(4)
    Dni_Busqueda = input("Introduce el D.N.I. del cliente. ")
    # Dnis=len(My_List)
    # print(Dnis)
    # time.sleep(3)
    for i in range(len(My_List)):
        if Dni_Busqueda == My_List[0][i]:
            print(My_List[0][i], My_List[1][i], My_List[2][i], My_List[3][i])
            respuesta = input(print("Este es el registro que quiere borrar (s/n"))
            if respuesta == "s" or respuesta == "S":
                del My_List[0][i], My_List[1][i], My_List[2][i], My_List[3][i]
                print("Borrado...")
                print("Número de registros despues de borrar", My_List)
                time.sleep(5)
                break
            else:
                continue
    else:
        print("El D.N.I. no existe. ")
        time.sleep(2)

def Modificaciones():
    print("Estás en la parte de modificaciones...")
    time.sleep(3)

def Listado():
    contador = 0
    for i in range(len(My_List)):
        for j in range(len(My_List[i])):
            contador += 1
        print(contador)
        time.sleep(3)
        break
    for i in range(contador):
        print("D.N.I. ", My_List[0][i])
        print("Nombre: ", My_List[1][i])
        print("Apellidos: ", My_List[2][i], My_List[3][i])

# while Eleccion != 5:
while True:
    os.system("clear")
    print("1.- Altas ")
    print("2.- Bajas ")
    print("3.- Modificacines ")
    print("4.- Listado de clientes ")
    print("5.- Salir ")
    print("")
    Eleccion = int(input(print("Elija una opción. ")))

    if Eleccion == 1:
        Altas()
    if Eleccion == 2:
        Bajas()
    if Eleccion == 3:
        Modificaciones()
    if Eleccion == 4:
        Listado()
    if Eleccion == 5:
        break