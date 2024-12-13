# Herencia

class Vehiculo:
    def __init__(self, marca, modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    def __str__(self):
        return f'{self.marca} {self.modelo} {self.color}'
class Auto(Vehiculo):
    def __init__(self, marca, modelo,color,numero_llantas):
        super().__init__(marca,modelo,color)
        self.numero_llantas = numero_llantas

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.color} {self.numero_llantas}'

class Camion(Vehiculo):
    def __init__(self, marca, modelo,color,numero_llantas):
        super().__init__(marca,modelo,color)
        self.numero_llantas = numero_llantas

    def __str__(self):
        return f'{self.modelo} {self.color} {self.numero_llantas}'
# creación de varios  objetos
mi_auto = Auto('Chevrolet','SAIL','Red',4)
mi_camion = Camion('HINO','GH','BLANCO',6)
print(mi_auto)
print("la marca de mi objeto 1",mi_auto.marca)
print(mi_camion.marca)
print(mi_camion.numero_llantas)
print(mi_camion.color)
print(mi_camion.marca)
print(mi_camion.numero_llantas)