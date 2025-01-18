# clase vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.__modelo = modelo #atributo privado

    def obtener_modelo(self):
        return self.__modelo

    def descripcion(self):
        return f"Modelo: {self.__modelo}, Marca: {self.marca}"

class Auto(Vehiculo):

    def __init__(self, marca, modelo,puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def descripcion(self): # polimorfismo
        return f"Marca {self.marca}, Modelo {self.obtener_modelo()},Puertas: {self.puertas}"

def mostrar_descripcion(vehiculo):
    print(vehiculo.descripcion())

# creacion de objetos
vehiculo = Vehiculo("Mazda","modelo 323")
auto =Auto("Marca A","Modelo A","Puertas A")

# mostrar la encapsulacion
print(vehiculo.obtener_modelo())

# mostar el poli
mostrar_descripcion(auto)
#mostrar_descripcion(vehiculo)