from manejadorPedido import manePedido as pedido
from manejadorRepartidor import maneRepartidor as repartidor

def menu():
    salir = False
    opcion = 0
    while not salir:
        print('\n-------------MENU DE OPCIONES------------')
        print('\n1- Pedidos de entrega pendientes.')
        print('\n2- Imprimir listado de pedidos.')
        print('\n3- Determinar repartiores repetidos.')
        print('\n4- Listado de repartidores.')
        print('\n5- Salir.')
        opcion = int(input('\nIngrese opcion: '))

        if opcion == 1:
            identi = input('\nIngrese id de repartidor: ')
            pedi.buscar(identi)

        if opcion == 2:
            nro = input('\nIngrese nro de repartidor para ver los pedidos: ')
            repar.mostrar(nro)
            print('\nNro de pedido    Descripcion   Cantidad  Precio Unitario  Total')
            pedi.mostrar(nro)

        if opcion == 3:
            repar.repetidos(pedi)

        if opcion == 4:
            repar.calcularImporte(pedi)
            repar.ranking()

        if opcion == 5:
            salir = True




if __name__ == '__main__':
    pedi = pedido(11)
    repar = repartidor()
    pedi.testManejador()
    repar.testManejador()
    menu()