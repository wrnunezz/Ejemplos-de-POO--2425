# ejemplo de clase , objeto, herencia, poli, encapsula
# clase vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.__modelo = modelo # atributo privado

    def obtener_modelo(self):
        return self.__modelo
    def descripcion(self):
        return f" marca {self.marca} modelo {self.__modelo}"
class Auto(Vehiculo):
    def __init__(self, marca, modelo,numeropuertas):
        super().__init__(marca,modelo)
        self.numeropuertas = numeropuertas
    def descripcion(self):
        return f" marca {self.marca} modelo {self.obtener_modelo()} puertas {self.numeropuertas}"

def mostrar_descripcion(vehiculo):
    print(vehiculo.descripcion())


# creación de objeto
vehiculo1 = Vehiculo('Mercedes', 'BMW')
auto1 = Auto('Chevolet', 'sail', 5)
print(vehiculo1.marca)
# mostrar encaps
print(vehiculo1.obtener_modelo())
# mostrar polimorfirmo

mostrar_descripcion(vehiculo1)
mostrar_descripcion(auto1)




