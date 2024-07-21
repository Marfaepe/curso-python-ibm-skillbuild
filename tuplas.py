tupla_vacia =()

tupla_sin_parentesis = 1,2,3,4,'a','b','c','d'

# Crear una tupla con un solo elemento siempre con la coma ,
tupla_con_un_elemento = (8,)

mi_tupla = (1,2,3,4,'a','b','c','d')

#acceder a los elementos de una tupla
print(mi_tupla[0])
print(mi_tupla[-1])
print(mi_tupla[1:4])
print(mi_tupla[0:6:2]) 



#Operaciones y métodos comunes con las tuplas
#Puedes concatenar dos o más tuplas usando el operador +.
tupla1 = (7,8,9)
tupla2 = ('q','r','s')
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)


#Puedes repetir una tupla usando el operador *.
tupla_repetida = tupla1 * 3
print (tupla_repetida)


#operador in para verificar si un elemento está en la tupla.
print(2 in mi_tupla)
print('z' in mi_tupla)

#desempaquetar tuplas en variables individuales.
a, b, c = (1, 2, 3)
print(a)  # Salida: 1
print(b)  # Salida: 2
print(c)  # Salida: 3


#Usa la función len() para obtener la longitud de una tupla
print(len(tupla_concatenada))


#TUPLAS ANIDADAS
#convertir una tupla en lista
mi_lista = list(mi_tupla)
print(mi_lista)

#Modificar la lista
mi_lista.append('nuevo')
print(mi_lista)

#convertir la lista en una nueva tupla
mi_tupla_modificada = tuple(mi_lista)
print(mi_tupla_modificada)


# Desempaquetado avanzado con tuplas
tupla_avanzada = (1, (2, 3), 4)

# Desempaquetado en una sola línea
a, (b, c), d = tupla_avanzada
print(a)  # Salida: 1
print(b)  # Salida: 2
print(c)  # Salida: 3
print(d)  # Salida: 4


#TUPLAS COMO CLAVES DE DICCIONARIOS
#Usar una tupla como clave de diccionario
diccionario ={
    (1,2): 'Valor1', 
    (3,4): 'valor2'
}
# Acceder a un valor usando una tupla como clave
print(diccionario[(1, 2)])  # Salida: valor1



#TUPLAS Y FUNCIONES

#funcion quedevuelve una tupla

def calcular_datos(a, b):
    suma = a + b
    producto = a * b
    return suma, producto

# Llamar a la función y desempaquetar los valores devueltos
resultado_suma, resultado_producto = calcular_datos(5, 3)
print("Suma:", resultado_suma)  # Salida: Suma: 8
print("Producto:", resultado_producto)  # Salida: Producto: 15