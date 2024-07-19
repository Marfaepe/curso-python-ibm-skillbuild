#Cuadrados de los primeros 5 números enteros
cuadrados = [x ** 2 for x in range(1,6)]
print('Cuadrados de los primeros números enteros: ', cuadrados)


#Números pares en un rango del 1 al 20
numpares = [x for x in range(1,21) if x % 2 ==0]
print('numeros pares del 1 al 20: ', numpares)


#Palabras convertidas en mayúsculas
palabras = ['saludos', 'estructura', 'mundo']
mayusculas = [palabra.upper() for palabra in palabras]
print('Palabras en mayúsculas: ', mayusculas)