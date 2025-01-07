class Persona:
    # constructor
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre},{self.apellido} y mi edad es:  {self.edad}")
# instanciar un objeto
persona = Persona('Pepito', 'Perez', '23')
persona2= Persona('Juan', 'Cajaz', '25')
print(persona2.nombre)
# Uso de los metodos
persona.saludar()
persona2.saludar()
# imprimir
print(persona.nombre)