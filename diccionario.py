mi_diccionario ={
    'nombre': 'Pedro',
    'edad': 25,
    'ciudad': 'Bilbao',
    'profesión': 'Ingeniero'
   
}
nombre = mi_diccionario['nombre']
edad = mi_diccionario['edad']
profesion = mi_diccionario['profesión']
print(nombre, edad, profesion)

#Agregar o modificar elementos
mi_diccionario['edad'] = 31
print(edad)
mi_diccionario['apellido'] = 'Lopéz'
apellido = mi_diccionario['apellido']
print(mi_diccionario)

#Eliminar elementos
# Usar el método pop para eliminar y obtener el valor eliminado

edad = mi_diccionario.pop('edad')

# Usar del para eliminar sin obtener el valor
del mi_diccionario["ciudad"]

# Usar keys(), values(), items()
claves  = mi_diccionario.keys()
valores = mi_diccionario.values()
elementos = mi_diccionario.items()

# Usar get()
nombre = mi_diccionario.get('nombre')
altura = mi_diccionario.get('altura', 'no especificado')

#Usar update()
otros_datos = {
    'pais' : 'España'
}
mi_diccionario.update(otros_datos)

     