#Crear una lista vacía
lista = []

#Crear una lista con varios elementos
lista = [ 1, 2, 3,4,5]

# Crear una lista con diferentes tipos de elementos
mi_lista = [1, "dos", 3.0, True]

#Métodos básicos de las listas 
mi_lista = [3,1,4,1,5,9]

mi_lista.append(2) #Añadir un elemento al final
print("Después de append:", mi_lista)

mi_lista.remove(1) #Elimina el primer elemento cuyo valor sea 1
print("Después de remove:", mi_lista)

ultimo_elemento = mi_lista.pop()#Eliminar y retornar el último elelmento
print("Después de pop:", mi_lista)
print("Último elemento eliminado:", ultimo_elemento)

mi_lista.sort() #ordena la lista
print("Después de sort:", mi_lista)

mi_lista.reverse() #invierte la lista
print("Después de reverse:", mi_lista)

lista_nueva = [10, 20, 30, 40, 50]
lista_nueva.clear()
print(lista_nueva)  # Output: []

conjunto = {1, 2, 3, 4, 5}
print(conjunto)  # Output: {1, 2, 3, 4, 5}
conjunto.clear()
print(conjunto)  # Output: set()

print("Uso de 'del':")
lista_2 = [10, 20, 30, 40, 50]
print("Lista original:", lista)
del lista_2[2]  # Elimina el elemento en el índice 2
print("Lista después de 'del lista[2]':", lista_2)
del lista_2[1:3]  # Elimina los elementos desde el índice 1 hasta el índice 2
print("Lista después de 'del lista[1:3]':", lista_2)