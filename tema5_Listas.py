'''
una lista es una secuencia de elementos
[]
'''

lista = ["Mario", 33, 29, 5, True, "German", 20, 9]
print(lista)
print(lista[1])
print(lista[2])
print(lista[-1])
print(lista[0:3])
print(lista[3:])

lista.append("vargas")
print(lista)

lista.insert(2,"Media")
print(lista)
lista.extend(["UNO",1,1,False])
print(lista)
lista.remove(33)
print(lista)
lista.pop()
print(lista)

lista2 = ["TRES", "CUATRO"]
lista3 = lista + lista2
print(lista3)

print(lista2*4)
lista4 = [2,1,3,4,6]
print(lista4)
