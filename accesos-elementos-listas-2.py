mi_lista = [1, 2, 3, 4, 5]
otra_lista = list([10, 20, 30, 40])

#Indexación: Acceso a un elemento específico usando su índice. Los índices empiezan en 0.
mi_lista[0]  # Primer elemento: 1
mi_lista[-1] # Último elemento: 5

#Slicing: Obtener una sublista especificando un rango de índices.
sub_lista = mi_lista[1:4]  # Sublista desde el índice 1 hasta el 3: [2, 3, 4]

#Stride: Controlar el intervalo entre los elementos seleccionados en el slicing.
#lista[inicio:fin:stride]
sub_lista = mi_lista[0:5:2]  # [1, 3, 5]

