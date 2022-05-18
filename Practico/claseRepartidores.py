class Repartidor:
    def __init__(self,id,apellido,nombre,telefono,movilidad):
        self.__id = id
        self.__apellido = apellido
        self.__nombre = nombre
        self.__telefono = telefono
        self.__movilidad = movilidad
        self.__importe = 0

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.__id,self.__apellido,self.__nombre,self.__telefono,self.__movilidad,self.__importe)

    def getId(self):
        return self.__id
    def nombre(self):
        return self.__nombre
    def apellido(self):
        return self.__apellido
    def telefono(self):
        return self.__telefono
    def movi(self):
        return self.__movilidad

    def importe(self,importe):
        self.__importe += importe

    def __eq__(self,other):
        return self.__nombre == other.__nombre

    def __gt__(self,other):
        return self.__importe > other.__importe