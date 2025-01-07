# Herencia
class Animal:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso
    def eat(self):
        self.peso += 1
class Dog(Animal):
    def __init__(self, nombre, peso,sonido):
        super().__init__(nombre, peso)
        self.sonido = sonido

class Cat(Animal):
    def __init__(self, nombre, peso,sonido):
        super().__init__(nombre, peso)
        self.sonido = sonido

mi_perro = Dog("Peluchin",10,'Guaaaa')
mi_perro.eat()

print(mi_perro.peso)
print(mi_perro.nombre)
