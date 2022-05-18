import csv
import numpy as np
from clasePedidos import Pedidos as pedi

class manePedido:
    __cantidad = 0
    __dimension = 0
    __incremento = 11

    def __init__(self, dimension, incremento=11):
        self.__pedidos = np.empty(dimension, dtype=pedi)
        self.__cantidad = 0
        self.__dimension = dimension

    def __str__(self):
        s = ''
        for pedi in self.__pedidos:
            s += str(pedi) + '\n'
        return s

    def agregar(self, objeto):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__pedidos.resize(self.__dimension)
        self.__pedidos[self.__cantidad] = objeto
        self.__cantidad += 1

    def testManejador(self):
        archi = open('pedidos')
        reader = csv.reader(archi,delimiter=';')
        for i in reader:
            id = i[0]
            objeto = pedi(id,i[1],i[2],i[3],i[4],i[5])
            self.agregar(objeto)
        archi.close()

    def buscar(self,identi):
        for pedi in self.__pedidos:
            if identi == pedi.getId():
                if(pedi.getEstado() == 'N'):
                    print(pedi)

    def mostrar(self,nro):
        for pedi in self.__pedidos:
            if(nro == pedi.getId()):
                print(pedi.getId(),    pedi.getdescripcion(), pedi.getcantidad(), pedi.precio(),pedi.total())

    def buscar2(self,id):
        i = 0
        while i < len(self.__pedidos):
            if(self.__pedidos[i].getId() == id):
                if(self.__pedidos[i].getEstado() == 'N'):
                    print('\n El repartidor con id {} no se puede eliminar porque todavia tiene pedidos pendientes.'.format(id))
            i +=1

    def calcular(self,id):
        i,cont = 0,0
        while (i < len(self.__pedidos)):
            if(self.__pedidos[i].getId() == id):
                cont += 1
            i+=1
        return cont,self.__pedidos[i].total()