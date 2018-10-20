# autor: J. Jesus Beltran Mundo #
animal = ("animales")
animales = ["raton","gato","perro","puma","leon"]

#(Append) Agregando un elemnto
print ("Append")
animesles = ["raton","gato","perro","puma","leon"]
animales.append("lobo")
print (animales)

#(insert) insertando un elemento
print ("insert")
animales.insert(2, "tigre")
print (animales)

# (count) contando elementos en una lista (RETORNA)
print ("count")
animales = ["raton","gato","perro","puma","leon"]
resultado = animales.count("gato")
print (resultado)

#(Index) Devuelve el indice del primer elemento con el valor especifico
print ("Index")
print(animales.index("gato"))

#(Remove) Elimina el primer elemento con el valor especificado
print ("Remove")
animales.remove("gato")
print (animales)

#(Pop) elimina elelemento en la posicion especificada
print ("Pop")
resultado = animales.pop(1)
print (resultado)

print (animales)

#(Extend) agrega los elementos de una lista (ocualquier iterable), al final de la lista actual
print ("Extend")
animales = ["raton","gato","perro","puma","leon"]
lista2 = ("conejo","liebre")
animales.extend(lista2)
print (animales)

#(Reverse) invierte el orden de la lista
print("Reverse")
animales = ["raton","gato","perro","puma","leon"]
animales.reverse()
print (animales)

#(sort) Ordena la lista (alfabeticamente)
print ("sort")
animales = ["raton","gato","perro","puma","leon"]
animales.sort()
print (animales)

#(Copy) Devuelve una copia de la lista (copie lista de animales)
print ("Copy")
animales = ["raton","gato","perro","puma","leon"]
animales.copy()
print (animales)

#(Clear) Elimina todos los elementos de la lista (Elimina todos los elementos de la lista animales)
print ("Clear")
animlaes = ["raton","gato","perro","puma","leon"]
animales.clear()
print (animales)




























