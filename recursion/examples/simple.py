def suma_naturales(N: int) -> int:
    """
    Calcula la suma de los primeros N números naturales.
    
    Args:
        N (int): El número hasta el cual se desea calcular la suma.
        
    Returns:
        int: La suma de los primeros N números naturales.
    """
    if N == 1:  # Caso base: Cuando N es 1, la suma es 1
        return 1
    else:
        return N + suma_naturales(N - 1)  # Llamada recursiva reduciendo N

# Ejemplo de uso
resultado: int = suma_naturales(5)
print(f"La suma de los primeros 5 números naturales es: {resultado}")
# Salida esperada: "La suma de los primeros 5 números naturales es: 15"

# Caso de prueba 1: Suma de los primeros 1 número natural
resultado: int = suma_naturales(1)
print(f"La suma de los primeros 1 número natural es: {resultado}")
# Salida esperada: "La suma de los primeros 1 número natural es: 1"

# Caso de prueba 2: Suma de los primeros 10 números naturales
resultado: int = suma_naturales(10)
print(f"La suma de los primeros 10 números naturales es: {resultado}")
# Salida esperada: "La suma de los primeros 10 números naturales es: 55"

# Caso de prueba 3: Suma de los primeros 20 números naturales
resultado: int = suma_naturales(20)
print(f"La suma de los primeros 20 números naturales es: {resultado}")
# Salida esperada: "La suma de los primeros 20 números naturales es: 210"
