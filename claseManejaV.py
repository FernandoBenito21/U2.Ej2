from claseViajero import *
import csv

class manejaViajero:
    def __init__(self):
        self.__Viajeros=[]
    def agregarViajero(self,unViajero):
        self.__Viajeros.append(unViajero)
    def archivero(self):
        archivo= open('Viajeros_ej2.csv')
        lector= csv.reader(archivo,delimiter=',')
        for elemento in lector:
            num= elemento[0]
            dni= elemento[1]
            nom= elemento[2]
            apellido= elemento[3]
            millas= int(elemento[4])
            unViajero= ViajeroFrecuente(num,dni,nom,apellido,millas)
            self.agregarViajero(unViajero)
        archivo.close()
    def buscaViajero(self,num):
        i=0
        Pos= None
        bandera= False
        while ((bandera==False) and (i<len(self.__Viajeros))):
            if self.__Viajeros[i].getNum()==num:
                bandera=True
                Pos=i
            else:
                i+=1
        return Pos
    def getMillas(self,n):
        return(self.__Viajeros[n].cantidadTotalMillas())
    def acumularMillas(self,extras,n):
        m= self.__Viajeros[n].acumularMillas(extras)
        return m
    def canjearMillas(self,cant,n):
        self.__Viajeros[n].canjearMillas(cant)
        return self.__Viajeros[n].cantidadTotalMillas()