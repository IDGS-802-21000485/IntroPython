'''
las tuplas son inmutables
()
'''

tupla = ("UNO", "DOS","TRES")
print(tupla)
print(type(tupla))

tuplasVariosD=(12,True,23.6,"Nombre",12+3j)
print(tuplasVariosD)

tuplasConTuplas = (1,2,3,4,(1,2,3))
print(tuplasConTuplas)

print(tuplasVariosD[3])
print(tuplasVariosD[-2])
print(tuplasVariosD[0:2])

a,b,c = tupla
print(a)
print(b)
print(c)