# encapsulamiento

class Cuenta_Bancaria:
    def __init__(self, saldo_general):
        self.__saldo =saldo_general

    def depositar(self,valor):
        self.__saldo +=valor   ## saldo = saldo + valor

    def retiro(self,valor):
        self.__saldo -=valor

    def obtener_saldo(self):
        return self.__saldo

# creo la insta
mi_cuenta =Cuenta_Bancaria(30)
print(mi_cuenta.obtener_saldo())

mi_cuenta.depositar(30)
print(mi_cuenta.obtener_saldo())

mi_cuenta.retiro(10)
print(mi_cuenta.obtener_saldo())