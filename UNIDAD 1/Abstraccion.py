# Abstraccion

from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

    def descripcion(self):
        return "Soy una figura geo"
#clase concreta
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio ** 2

# clase concreta
class rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

#insta obj
mi_circulo = Circulo(8)
mi_circulo.area()
print(f"Area de un circulo : {mi_circulo.area()}")
mi_rectangulo = rectangulo(5, 5)
print(f"Area de un recta : {mi_rectangulo.area()}")


