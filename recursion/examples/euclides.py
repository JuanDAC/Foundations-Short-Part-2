def euclides(a: int, b: int) -> int:
    """
    Calcula el máximo común divisor (MCD) de dos números enteros a y b utilizando el algoritmo de Euclides.
    
    Args:
        a (int): El primer número entero.
        b (int): El segundo número entero.
        
    Returns:
        int: El MCD de a y b.
    """
    pass

# Caso de prueba 1: MCD de 48 y 18
num1: int = 48
num2: int = 18
mcd: int = euclides(num1, num2)
print(f"MCD de {num1} y {num2} es {mcd}")
# Salida esperada: "MCD de 48 y 18 es 6"

# Caso de prueba 2: MCD de 72 y 36
num1: int = 72
num2: int = 36
mcd: int = euclides(num1, num2)
print(f"MCD de {num1} y {num2} es {mcd}")
# Salida esperada: "MCD de 72 y 36 es 36"

# Caso de prueba 3: MCD de 105 y 45
num1: int = 105
num2: int = 45
mcd: int = euclides(num1, num2)
print(f"MCD de {num1} y {num2} es {mcd}")
# Salida esperada: "MCD de 105 y 45 es 15"

# Caso de prueba 4: MCD de 17 y 8
num1: int = 17
num2: int = 8
mcd: int = euclides(num1, num2)
print(f"MCD de {num1} y {num2} es {mcd}")
# Salida esperada: "MCD de 17 y 8 es 1"
