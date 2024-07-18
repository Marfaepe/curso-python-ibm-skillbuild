#Encontrar el mínimo de estos dos números
a = 2
b = 4

def minunum(a,b):
    if a<=b:
        return a
    else:
        return b
print(minunum(a,b))    


#Invertir palabras de una cadena dada

str = 'código de práctica de prueba de geeks'
str = 'geeks de prueba de práctica de código'

def rev_sentence(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence

if __name__ == "__main__":
    input = 'geeks quiz practice code'
    print(rev_sentence(input))

#Realiza la suma de los elementos de la tupla

test_tup= (7,8,9,1,10,7)
print('La tupla original es: ',test_tup)
res = sum(test_tup)
print('La suma de los elementos de la tupla son:', res)


# Escriba un código que calcule una lista de números proporcionados.

def list_sum(num_list):
    if len(num_list)==1:
        return num_list[0]
    else:
            # Caso recursivo: sumar el primer elemento con la suma de los demás elementos
        return num_list[0] + list_sum(num_list[1:])
    
# Ejemplo de uso de la función para calcular la suma de una lista de números
print(list_sum([3, 5, 8, 9, 9]))

#Escriba un código que desordene al azar una lista.
from random import shuffle
exil = ['skyrim', 'pertenece', 'A', 'Los', 'Nórdicos']
shuffle(exil)
print(exil)



   