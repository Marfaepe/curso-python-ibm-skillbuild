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