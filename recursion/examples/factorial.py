def factorial(n: int) -> int:
    """
    Calcula el factorial de un número entero no negativo n.
    
    Args:
        n (int): El número entero para calcular su factorial.
        
    Returns:
        int: El factorial de n.
    """
    pass

# Caso de prueba 1: Factorial de 0
numero: int = 0
resultado: int = factorial(numero)
print(f"Factorial de {numero} es {resultado}")
# Salida esperada: "Factorial de 0 es 1"

# Caso de prueba 2: Factorial de 1
numero: int = 1
resultado: int = factorial(numero)
print(f"Factorial de {numero} es {resultado}")
# Salida esperada: "Factorial de 1 es 1"

# Caso de prueba 3: Factorial de 5
numero: int = 5
resultado: int = factorial(numero)
print(f"Factorial de {numero} es {resultado}")
# Salida esperada: "Factorial de 5 es 120"

# Caso de prueba 4: Factorial de 10
numero: int = 10
resultado: int = factorial(numero)
print(f"Factorial de {numero} es {resultado}")
# Salida esperada: "Factorial de 10 es 3628800"
