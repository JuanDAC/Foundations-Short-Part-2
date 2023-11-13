
# Empaquetar
mi_tupla = 1, 2, 3

# Desempaquetar
a, b, c = mi_tupla


name = ("John", "Doe")
contact = ("john@example.com", "55-555-5555")

inpack = (*name, *contact) # ('John', 'Doe', 'john@example.com', '55-555-5555')

inpack, a, b, c, mi_tupla