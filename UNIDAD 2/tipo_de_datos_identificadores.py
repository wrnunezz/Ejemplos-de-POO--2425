class Triangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura)/2

base=10
altura= 20

triangulo = Triangulo(base,altura)
resultado = triangulo.area()
print("La respuesta",resultado)

