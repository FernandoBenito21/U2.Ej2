from claseViajero import *
from claseManejaV import *

if __name__ == '__main__':
    lista= manejaViajero()
    lista.archivero()
    num= input('Ingresar numero de viajero:')
    n= lista.buscaViajero(num)
    opcion= None
    if (n == None):
        print("El numero de viajero no existe")
    else:
        while (opcion != '0'):
            opc = input('''...Menu...
                0).Concluir
                1).Consultar cantidad de millas
                2).Acumular Millas
                3).Canjear millas
                ''')
            if opcion== '1':
                print("Cantidad total de millas: ", lista.getMillas(n))
            elif opcion== '2':
                extras= int(input('Ingrese la cantidad de millas a sumar:'))
                print("Nuevo total de millas:", lista.acumularMillas(extras, n))
            elif opcion== '3':
                cant = int(input('Ingresar cantidad de millas a canjear:'))
                lista.canjearMillas(cant, n)