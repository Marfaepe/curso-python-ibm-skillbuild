#Ejemplo 1 de lista anidada básica
lista_anidada = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print('Lista aniadada básica: ', lista_anidada)

#acceder a un elemento de la sub-lista
primer_elemento = lista_anidada[0][0]

#acceder a la sublista específica
segunda_sublista = lista_anidada[1]
print('Segunda sublits: ', segunda_sublista)

# Acceder a un elemento específico en una sublista
elemento_especifico = lista_anidada[2][1]
print("Elemento en la tercera sublista, segunda posición:", elemento_especifico)


# Ejemplo 2: Modificar Elementos en una Lista Anidada

lista_anidada[0][1]=20 #cambia el vval9or en la primera sublista
print('Lista anidada después de modificar: ', lista_anidada)

# Añadir una nueva sublista
lista_anidada.append([10, 11, 12])
print("Lista anidada después de añadir una nueva sublista:", lista_anidada)

# Eliminar una sublista
del lista_anidada[1]
print("Lista anidada después de eliminar una sublista:", lista_anidada)