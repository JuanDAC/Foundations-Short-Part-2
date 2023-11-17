from typing import Tuple, Union

def suma_tupla(tupla: Tuple[Union[int, float]]) -> Union[int, float]:
    """
    Calcula la suma de los elementos de una tupla que contiene números enteros o de punto flotante.
    
    Args:
        tupla (Tuple[Union[int, float]]): La tupla de números enteros o de punto flotante.
        
    Returns:
        Union[int, float]: La suma de los elementos de la tupla.
    """
    pass

# Ejemplo de uso
datos: Tuple[int] = (1, 2, 3, 4, 5)
suma: int = suma_tupla(datos)
print(f"Suma de los elementos de la tupla: {suma}")
# Salida esperada: "Suma de los elementos de la tupla: 15"

# Caso de prueba 1: Tupla vacía
datos: Tuple = ()
suma: int = suma_tupla(datos)
print(f"Suma de los elementos de la tupla: {suma}")
# Salida esperada: "Suma de los elementos de la tupla: 0"

# Caso de prueba 2: Tupla con enteros positivos
datos: Tuple[int] = (1, 2, 3, 4, 5)
suma: int = suma_tupla(datos)
print(f"Suma de los elementos de la tupla: {suma}")
# Salida esperada: "Suma de los elementos de la tupla: 15"

# Caso de prueba 3: Tupla con números de punto flotante
datos: Tuple[float] = (0.5, 1.5, 2.5, 3.5)
suma: float = suma_tupla(datos)
print(f"Suma de los elementos de la tupla: {suma}")
# Salida esperada: "Suma de los elementos de la tupla: 8.0"

# Caso de prueba 4: Tupla con números enteros y de punto flotante mezclados
datos: Tuple[Union[int, float]] = (1, 2.5, 3, 4.5, 5)
suma: Union[int, float] = suma_tupla(datos)
print(f"Suma de los elementos de la tupla: {suma}")
# Salida esperada: "Suma de los elementos de la tupla: 16.0"
