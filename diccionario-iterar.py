# Crear un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Iterar sobre las claves
print("Claves:")
for clave in mi_diccionario:
    print(clave)

# Iterar sobre los valores
print("\nValores:")
for valor in mi_diccionario.values():
    print(valor)

# Iterar sobre pares clave-valor
print("\nPares clave-valor:")
for clave, valor in mi_diccionario.items():
    print(f'{clave}: {valor}')


# Diccionario anidado
alumnos = {
    "Juan": {"edad": 30, "ciudad": "Madrid"},
    "Ana": {"edad": 25, "ciudad": "Barcelona"}
}

# Acceder a elementos en un diccionario anidado
edad_juan = alumnos["Juan"]["edad"]  # 30
ciudad_ana = alumnos["Ana"]["ciudad"]  # "Barcelona