# Polimorfismo
# diferentes clases tengan el mismo metodo , pero comportamientos diferentes
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        # metodo genérico
        raise NotImplementedError("Este metdo debe ser impl por la subclase")

#clase hija (subclase)
class Dog(Animal):
    def __init__(self, nombre,raza):
        super().__init__(nombre)
        self.raza = raza

    def hacer_sonido(self):
        # Sobreescribir
        return f"{self.nombre} {self.raza} dice : WAOOOOO"
class Cat(Animal):
    def __init__(self, nombre,sonido):
        super().__init__(nombre)
        self.sonido = sonido


    def hacer_sonido(self):
        return f"{self.nombre}, {self.sonido} dice : Miauuu"

# funcion para aplicar polimorfismo

def mostrar_sonido(animal):
    print(animal.hacer_sonido())

# crear los objetos
mi_perro = Dog("Peluchin","Chiguagua")

#uso del polimorfismo
mostrar_sonido(mi_perro)
