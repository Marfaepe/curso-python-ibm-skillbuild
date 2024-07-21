mi_diccionario = {
    "nombre": "Martin",
    "edad": 50,
    "ciudad": "Londres"
}

# mostrar las claves, valores y pares clave-valor
print('Claves:')
for clave in mi_diccionario.keys():
    print(clave)

print('\nValores:')
for valor in mi_diccionario.values():
    print(valor)

print('\nPares clave-valor:')
for clave, valor in mi_diccionario.items():
    print(f'{clave}: {valor}')   

# Uso de .get() para acceder a valores con un valor predeterminado
print("\nValor para la clave 'nombre':", mi_diccionario.get("nombre"))
print("Valor para la clave 'telefono' con valor predeterminado:", mi_diccionario.get("telefono", "No disponible"))

# Uso de .pop() para eliminar un par clave-valor
edad = mi_diccionario.pop("edad", "No disponible")
print("\nEdad eliminada:", edad)
print("Diccionario después de eliminar 'edad':", mi_diccionario)

# Uso de .popitem() para eliminar el último par clave-valor agregado
item = mi_diccionario.popitem()
print("\nPar clave-valor eliminado con popitem():", item)
print("Diccionario después de eliminar el último par:", mi_diccionario)

# Uso de .update() para actualizar el diccionario con otro diccionario
mi_diccionario.update({"edad": 31, "pais": "España"})
print("\nDiccionario actualizado con .update():", mi_diccionario)
