class Pedidos:
    def __init__(self,id,nro,des,cant,precio,estado):
        self.__id = id
        self.__nroPedido = nro
        self.__descripcion = des
        self.__cantidad = int(cant)
        self.__precio = int(precio)
        self.__estado = estado

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.__id,self.__nroPedido,self.__descripcion,self.__cantidad,self.__precio,self.__estado)

    def getId(self):
        return self.__id
    def getEstado(self):
        return self.__estado
    def getnro(self):
        return self.__nroPedido
    def getdescripcion(self):
        return self.__descripcion
    def getcantidad(self):
        return self.__cantidad
    def precio(self):
        return self.__precio
    def total(self):
        return (self.__cantidad * self.__precio)