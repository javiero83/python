'''
CUENTA BANCARIA

1. Clase Persona
    atributos: nombre y apellido

2 Clase Cliente
    1. Hereda persona
    2.numero_cuenta y balance
    3. metodos: uno para imprimir
    4. metodos: depositar(), retirar()

3. codigo para elegir Depositar, Retirar o Salir
4. mantener balance, no puede retirar mas delo que tiene.

recomendacion
    1. funcion CREAR_CLIENTE()
    2 funcion INICIO()   [loop]

'''
clientes = {}

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def imprimir_balance(self):
        print(f'Balance: {self.balance}')


    def depositar(self, cantidad):
        self.balance = self.balance + cantidad
        print('Cantidad depositada!')
        print(f'Nuevo saldo: {self.balance}')
        return self.balance

    def retirar(self, cantidad):
        if self.balance >= cantidad:
            self.balance = self.balance - cantidad
            print('Operacion efectuada...')
            print(f'Nuevo Saldo: {self.balance}')
        else:
            print('Saldo no suficiente...')

def crear_cliente(alias, nombre, apellido, numero_cuenta, balance):

    cliente = Cliente(nombre, apellido, numero_cuenta, balance)
    clientes[alias] = cliente
    print(f'Cliente "{alias}, no. de cuenta: {numero_cuenta}" creado!')

def mostrar_clientes():
    print('CLIENTES REGISTRADOS')
    for alias,cliente in clientes.items():
        print(f' Cliente: {alias}, Numero de Cuenta: {cliente.numero_cuenta}')

def inicio():
    ope = 0

    while ope != 6:
        print('''
            *****************************
            BANCO MI ALEGRIA:
            *****************************
            Opciones:
            [1] Depositar
            [2] Retirar
            [3] Imprimir Balance
            [4] Crear Cliente
            [5] Lista Clientes
            [6] Salir\n
        ''')
        ope = int(input('Que operacion desea realizar: '))

        if ope == 1:
            print('''
            ****************
            DEPOSITAR
            **************** 
            ''')
            alias = input('A que alias desea depositar?')
            cantidad = int(input('Que cantidad desea depositar?: '))

            if alias in clientes:
                clientes[alias].depositar(cantidad)

            else:
                print('Ese alias no existe')

        elif ope == 2:
            print('''
                        ****************
                        RETIRAR
                        **************** 
                        ''')
            alias = input('A que alias desea retirar?')
            cantidad = int(input('Que cantidad desea retirar?: '))

            if alias in clientes:
                clientes[alias].retirar(cantidad)

            else:
                print('Ese alias no existe')
        elif ope == 3:
            print('''
            ****************
            IMPRIMIR BALANCE
            ****************''')
            alias = input('Alias que desea consultar:')
            if alias in clientes:
                clientes[alias].imprimir_balance()
            else:
                print('Ese alias no existe.')

        elif ope == 4:
            print('*************')
            print('CREAR CLIENTE')
            print('*************')
            nombre = input('Nombre del cliente: ')
            apellido = input('Apellido del cliente: ')
            numero_cuenta = input('Numero de cuenta: ')
            alias = f'{nombre}_{apellido}'
            crear_cliente(alias, nombre, apellido, numero_cuenta,0)
        elif ope == 5:
            print('''
            *****************
            LISTA DE CLIENTES
            *****************''')
            mostrar_clientes()

        elif ope != 6:
            print('Opcion no válida!')


inicio()