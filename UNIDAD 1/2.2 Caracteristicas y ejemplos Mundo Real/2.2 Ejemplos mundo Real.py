# clase producto

class  Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# clase pedidos
class Pedido:
    def __init__(self, identificador):
        self.identificador = identificador
        self.productos ={}

    def agregar_producto(self, producto,cantidad):
        if producto.nombre in self.productos:
            self.productos[producto.nombre]["cantidad"] += cantidad
        else:
            self.productos[producto.nombre] = {"producto":producto,"cantidad":cantidad}

    def eliminar_producto(self, producto,cantidad):
        if producto.nombre in self.productos:
            self.productos[producto.nombre]["cantidad"] -= cantidad
            if self.productos[producto.nombre]["cantidad"] <= 0:
                del self.productos[producto.nombre]
    def obtener_total(self):
        total = 0
        for item in self.productos.values():
            total += item["producto"].precio * item["cantidad"]
        return total

    def mostrar_detalles(self):
        print(f"pedidos del cliente o identificador #{self.identificador}")
        for nombre, detalle  in self.productos.items():
            producto = detalle["producto"]
            cantidad = detalle["cantidad"]
            print(f"{nombre}: Precio unityario {producto.precio} la cantidad {cantidad}")
        print(f"Total : {(self.obtener_total())}")

# crear los objetos
producto1 = Producto("Manzana", 100)
producto2 = Producto("Pera", 50)

pedido = Pedido("Pedro")
pedido.agregar_producto(producto1,100)
pedido.agregar_producto(producto2,30)

pedido.mostrar_detalles()

pedido.eliminar_producto(producto1,3)
pedido.mostrar_detalles()







