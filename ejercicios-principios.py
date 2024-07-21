print('Hola mundo')

#Suma de dis números
numero1 = input('Escrcibe el primer número')
numero2 = input('Esccribe el segundo número')

suma = int(numero1) + int(numero2)

print(f'La suma de {numero1} y {numero2} es {suma}')



#numeros pares
for numero in range(1,21):
    if numero % 2 == 0:
        print(numero)



#contar vocales de una cadena
cadena = input('Escrcibe una cadena de texto: ')
vocales = 'aeiouAEIOU'
contador =  0

for letra  in cadena:
    if letra in vocales:
        contador+=1
print(f"El número de vocales en la cadena es: {contador}")



