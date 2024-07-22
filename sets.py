#Crear un conjunto vacío
conjunto_vacio = set()

#crear conjunto con varios ekementos
mi_conjunto ={1,2,3,4,5}

# Agregar elementos
mi_conjunto.add(6)

# Eliminar elementos
mi_conjunto.remove(3)
mi_conjunto.discard(2)  # No genera error si el elemento no está presente
print(mi_conjunto)


#OPERACIONES CON CONJUNTOS
conjunto_a = {1, 2, 3}
conjuntp_b = {3, 4, 5}

#unión
union = conjunto_a | conjuntp_b
print(union)

#Intersección
interseccion = conjunto_a & conjuntp_b
print(interseccion)

#Diferencia
diferencia = conjunto_a - conjuntp_b
print(diferencia)


#Recorrer un Conjunto
for elemento in mi_conjunto:
    print(elemento)