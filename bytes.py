# Crear un objeto bytes usando un literal de bytes
byte_literal = b'Hola a todo el mundo'
print(byte_literal)

#convertir una cadena a bytes usando encode
cadena = 'Esta es una cadena que vamos a convertir a bytes'
bytes_convertidos = cadena.encode('utf-8')
print(bytes_convertidos)

#crea un objeto bytes a partir de una lista de enteros
byte_lista = bytes([90, 208, 192, 76])
print(byte_lista)

#Acceder a los elementos de un objeto bytes
byte_literal = b"Hola Mundo"
print(byte_literal[0])  # Salida: 72
print(byte_literal[1:4])  # Salida: b'ola'