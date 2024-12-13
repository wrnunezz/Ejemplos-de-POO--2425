#encapsulamiento

class cuentaBancaria:
    def __init__(self,saldo_general):
        self.__saldo=saldo_general  # atributo privado

    def depositar(self,valor):
        self.__saldo+=valor

    def retirar(self,valor):
        self.__saldo-=valor

    def obtener_saldo(self):
        return self.__saldo



mi_cuenta=cuentaBancaria(100)
#print(mi_cuenta.__saldo)
print(mi_cuenta.obtener_saldo())
mi_cuenta.depositar(50)
print(mi_cuenta.obtener_saldo())
mi_cuenta.retirar(20)
print(mi_cuenta.obtener_saldo())


