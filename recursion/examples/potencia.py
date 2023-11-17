def potencia(x: float, n: int) -> float:
    """
    Calcula la potencia de un número x elevado a un exponente n.
    
    Args:
        x (float): El número base.
        n (int): El exponente al cual elevar x.
        
    Returns:
        float: El resultado de x elevado a la n.
    """
    pass


# Caso de prueba 1: x^0
base: float = 5.0
exponente: int = 0
resultado: float = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es {resultado}")
# Salida esperada: "5.0 elevado a la 0 es 1.0"

# Caso de prueba 2: x^1
base: float = 3.0
exponente: int = 1
resultado: float = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es {resultado}")
# Salida esperada: "3.0 elevado a la 1 es 3.0"

# Caso de prueba 3: Potencia de 2^5
base: float = 2.0
exponente: int = 5
resultado: float = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es {resultado}")
# Salida esperada: "2.0 elevado a la 5 es 32.0"

# Caso de prueba 4: Potencia de 2^10
base: float = 2.0
exponente: int = 10
resultado: float = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es {resultado}")
# Salida esperada: "2.0 elevado a la 10 es 1024.0"
