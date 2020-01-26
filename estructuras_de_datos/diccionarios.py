# Diccionarios en Python

# Un diccionario es un mapa de valores, los cuales deben tener
# una llav. Los diccionarios se declaran con (llaves) {} o con la función dict()

# Cuando iteramos en diccionarios podemos hacerlo a través de las llaves, valores o ítems.

# Declarar diccionarios
diccionario = {}

# Agregar elementos a diccionarios
diccionario['primer_elemento'] = 'Hola'
diccionario['segundo_elemento'] = 'Adios'
diccionario['tercer_elemento'] = 'Hasta luego'
diccionario['cuarto_elemento'] = 'Hasta pronto'

# ---*------*------*------*------*------*------*------*------*---

calificaciones = {}
calificaciones['Algoritmica y programación II'] = 4.5
calificaciones['Matemática Estructural y lógica'] = 3
calificaciones['TI en las organizaciones'] = 3.8
calificaciones['Escritura Universitaria II'] = 4.3
calificaciones['Cálculo Diferencial'] = 3

# Iterar en llaves
print('\nKeys')
for key in calificaciones:
    print(key)
# Ó
print('\nKeys:')
for key in calificaciones.keys():
    print(key)

# Iterar en valores
print('\nValues:')
for value in calificaciones.values():
    print(value)

# Iterar ambos: tanto valores como llaves
print('\nItems:')
for key, value in calificaciones.items():
    print('{}: {}'.format(key, value))
