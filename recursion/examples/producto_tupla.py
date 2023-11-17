from typing import Tuple, Union

def producto_tupla(tupla: Tuple[Union[int, float]]) -> Union[int, float]:
    """
    Calcula el producto de los elementos de una tupla que contiene números enteros o de punto flotante.
    
    Args:
        tupla (Tuple[Union[int, float]]): La tupla de números enteros o de punto flotante.
        
    Returns:
        Union[int, float]: El producto de los elementos de la tupla.
    """
    pass

# Caso de prueba 1: Tupla vacía
datos: Tuple = ()
producto: int = producto_tupla(datos)
print(f"Producto de los elementos de la tupla: {producto}")
# Salida esperada: "Producto de los elementos de la tupla: 1"

# Caso de prueba 2: Tupla con enteros positivos
datos: Tuple[int] = (1, 2, 3, 4, 5)
producto: int = producto_tupla(datos)
print(f"Producto de los elementos de la tupla: {producto}")
# Salida esperada: "Producto de los elementos de la tupla: 120"

# Caso de prueba 3: Tupla con números de punto flotante
datos: Tuple[int] = (0.5, 1.5, 2.5, 3.5)
producto: int = producto_tupla(datos)
print(f"Producto de los elementos de la tupla: {producto}")
# Salida esperada: "Producto de los elementos de la tupla: 14.0625"

# Caso de prueba 4: Tupla con números enteros y de punto flotante mezclados
datos: Tuple[int] = (1, 2.5, 3, 4.5, 5)
producto: int = producto_tupla(datos)
print(f"Producto de los elementos de la tupla: {producto}")
# Salida esperada: "Producto de los elementos de la tupla: 84.375"
