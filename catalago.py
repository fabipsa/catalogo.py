class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre  # Atributo encapsulado
        self.__precio = precio   # Atributo encapsulado

    def obtener_nombre(self):
        return self.__nombre

    def obtener_precio(self):
        return self.__precio

    def __str__(self):
        return f"{self.__nombre}: ${self.__precio:.2f}"


class Camisa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.__talla = talla  # Atributo específico de Camisa

    def obtener_talla(self):
        return self.__talla

    def __str__(self):
        return f"Camisa - {super().__str__()}, Talla: {self.__talla}"


class Pantalon(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.__talla = talla

    def obtener_talla(self):
        return self.__talla

    def __str__(self):
        return f"Pantalón - {super().__str__()}, Talla: {self.__talla}"


class Zapato(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.__talla = talla

    def obtener_talla(self):
        return self.__talla

    def __str__(self):
        return f"Zapato - {super().__str__()}, Talla: {self.__talla}"


class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print(f"Categoría: {self.nombre}")
        for i, producto in enumerate(self.productos, start=1):
            print(f" {i}: {producto}")


class Tienda:
    def __init__(self):
        self.categorias = []

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def mostrar_categorias(self):
        print("Categorías disponibles:")
        for i, categoria in enumerate(self.categorias, start=1):
            print(f"{i}: {categoria.nombre}")

    def procesar_compra(self):
        self.mostrar_categorias()
        try:
            seleccion = int(input("Selecciona una categoría (número): ")) - 1
            if seleccion < 0 or seleccion >= len(self.categorias):
                raise ValueError("Selección no válida.")
            
            categoria_seleccionada = self.categorias[seleccion]
            categoria_seleccionada.mostrar_productos()

            producto_seleccionado = int(input("Selecciona un producto (número): ")) - 1
            if producto_seleccionado < 0 or producto_seleccionado >= len(categoria_seleccionada.productos):
                raise ValueError("Selección no válida.")
            
            producto = categoria_seleccionada.productos[producto_seleccionado]
            print(f"Has comprado: {producto}")
        except ValueError as e:
            print(e)
        except Exception as e:
            print("Ocurrió un error inesperado:", e)


# Ejemplo de uso
if __name__ == "__main__":
    tienda = Tienda()

    # Crear categorías
    categoria_camisas = Categoria("Camisas")
    categoria_pantalones = Categoria("Pantalones")
    categoria_zapatos = Categoria("Zapatos")

    # Agregar productos
    categoria_camisas.agregar_producto(Camisa("Camisa de rayas", 29.99, "M"))
    categoria_camisas.agregar_producto(Camisa("Camisa blanca", 19.99, "L"))
    
    categoria_pantalones.agregar_producto(Pantalon("Pantalón negro", 39.99, "32"))
    categoria_pantalones.agregar_producto(Pantalon("Pantalón azul", 34.99, "34"))

    categoria_zapatos.agregar_producto(Zapato("Zapato deportivo", 49.99, "42"))
    categoria_zapatos.agregar_producto(Zapato("Zapato de vestir", 59.99, "40"))

    # Agregar categorías a la tienda
    tienda.agregar_categoria(categoria_camisas)
    tienda.agregar_categoria(categoria_pantalones)
    tienda.agregar_categoria(categoria_zapatos)

    # Procesar compra
    tienda.procesar_compra()
