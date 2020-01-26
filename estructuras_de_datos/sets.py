# Uso de sets en Python
# Los sets son muy similares a las listas, pero estas no permiten elementos repetidos.

# Cuando trabajamos con sets, podemos realizar las operaciones básicas de conjuntos,
# esto quiere decir que se puede calcular los valores de intercepción, diferencia, unión.

# Declarar sets
s = set([1,2,3])
t = set([3,4,5])

# Operaciones con sets
s.union(t) # set([1,2,3,4,5])
s.intersection(t) # set([3])
s.difference(t) # set([1,2])
set(s).symmetric_difference(set(t)) # set([1,2,4,5])

1 in s # True
4 in s # False
1 in t # False
4 in t # True
3 not in s # False
6 not in s # True
