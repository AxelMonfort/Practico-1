import csv
from claseRepartidores import Repartidor as repa

class maneRepartidor:
    def __init__(self):
        self.__lista = []

    def __str__(self):
        s = ''
        for repa in self.__lista:
            s += str(repa) + '\n'
        return s

    def agregar(self,objeto):
        self.__lista.append(objeto)

    def testManejador(self):
        archi = open('repartidores')
        reader = csv.reader(archi,delimiter=';')
        for i in reader:
            id = i[0]
            objeto = repa(id,i[1],i[2],i[3],i[4])
            self.agregar(objeto)
        archi.close()

    def mostrar(self,nro):
        for repa in self.__lista:
            if (nro == repa.getId()):
                print('Apellido:{}          Nombre:{}          \n Telefono:{}         Tipo Movilidad:{}'.format(repa.apellido(),repa.nombre(),repa.telefono(),repa.movi()))


    def repetidos(self,pedido):
        for repa in self.__lista:
            cont = self.__lista.count(repa)
            if(cont != 1):
                print('\n Si hay repetidos')
                pedido.buscar2(repa.getId())

    def calcularImporte(self,pedido):
        cont,total,total2 = 0,0,0
        for repa in self.__lista:
            cont = pedido.calcular(repa.getId())
            total = cont[0] * cont[1]
            total2 = (total * 5) /100
            repa.importe(total2)

    def ranking(self):
        for repa in self.__lista:
            print(repa)
            print("-" * 71)