# Dictionary comprehension - list comprehension
# Dictionary comprehension y list comprehension nos permite escribir
# listas o diccionarios de forma más sencilla.

# Números pares [par, par, par, ...]
pares = []

for num in range(1,31):
    if num % 2 == 0:
        pares.append(num)

print(pares)

# List Comprehension:
# Esto mismo lo podemos expresar con una list comprehension
even = [num for num in range(1,31) if num % 2 == 0]
print(even)

# Números cuadrados en diccionarios {num: num^2}
cuadrados = {}
for num in range(1, 11):
    cuadrados[num] = num**2

print(cuadrados)

# Dictionary comprehension:
# Esto mismo lo podemos expresar con un dictionario comprehension
square = {num: num**2 for num in range(1,11)}
print(square)
