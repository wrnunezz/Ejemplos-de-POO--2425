#Polimorfimo
"""Permite q varias clases tengan metodos con el mismo nombre, pero con diferente comportamiento  """
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre  #atributo comun

    def hacer_sonido(self):
        print("llama")
        raise NotImplementedError("Este dee ser implemntado por la subclase")

class Dog(Animal):
    def __init__(self, nombre,raza):
        super().__init__(nombre)
        self.raza = raza

    def hacer_sonido(self):
        # sobreescribir
        return f"{self.nombre} {self.raza} dice:  waaaooo"

class Cat(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def hacer_sonido(self):
        return f"{self.nombre} {self.color} dice : Miau !"

# funcion de polimorfismo

def mostrar_sonido(animal):
    # llama al metodo de acuerdo al objeto
    print(animal.hacer_sonido())

# crear los objetos
mi_perro1 = Dog("Peluchin",'Labrador')
mi_gato1 = Cat("Pelusa","Negro")

mostrar_sonido(mi_perro1)
mostrar_sonido(mi_gato1)