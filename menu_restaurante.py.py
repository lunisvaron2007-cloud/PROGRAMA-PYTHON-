def calcular_precio_final(producto, categoria_objetivo, umbral):
    """
    Calcula el precio final aplicando 15% de descuento si:
    1. La categoría del producto == categoria_objetivo
    2. El precio base > umbral
    """
    nombre, categoria, precio_base = producto
    
    if categoria == categoria_objetivo and precio_base > umbral:
        precio_final = precio_base * 0.85  # Aplica 15% de descuento
    else:
        precio_final = precio_base  # Mantiene el precio base
    
    return precio_final

def mostrar_menu_con_promocion(menu, categoria_objetivo, umbral):
    print(f"{'Producto':<20} {'Categoría':<15} {'Precio Base':<15} {'Precio Final':<15}")
    print("-" * 65)
    
    for producto in menu:
        nombre, categoria, precio_base = producto
        precio_final = calcular_precio_final(producto, categoria_objetivo, umbral)
        print(f"{nombre:<20} {categoria:<15} ${precio_base:<14.2f} ${precio_final:<14.2f}")

# Matriz: [Nombre del Producto, Categoría, Precio Base] - mínimo 6 productos
menu_restaurante = [
    ["Hamburguesa Clásica", "Plato Fuerte", 25000],
    ["Pizza Pepperoni", "Plato Fuerte", 32000],
    ["Ensalada César", "Entrada", 18000],
    ["Limonada Natural", "Bebida", 8000],
    ["Cerveza Artesanal", "Bebida", 12000],
    ["Tiramisú", "Postre", 15000],
    ["Sopa del Día", "Entrada", 14000]
]

# Parámetros de la promoción
CATEGORIA_OBJETIVO = "Plato Fuerte"
UMBRAL_PRECIO = 20000

# Ejecutar
mostrar_menu_con_promocion(menu_restaurante, CATEGORIA_OBJETIVO, UMBRAL_PRECIO)