frutas = ["manzana", "banana"]
# Agregar un nuevo elemento al final de la lista
frutas.append("cereza")
# Insetar segun un indice
frutas.insert(1,"pera")
print(frutas)
# Elimina el ultimo elemento
frutas.pop()
# Elimina por indice
frutas.pop(1)
# Eliminar la primera aparicion
frutas.append("pera")
frutas.append("banana")
print(frutas)
frutas.remove("banana")
print(frutas)
# Ordenar la lista 
frutas.sort()
print(frutas)
# Ordernar la lista al reves 
frutas.append("cereza")
print(frutas)
frutas.reverse()
print(frutas)