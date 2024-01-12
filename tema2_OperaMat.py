num1 = 20
num2 = 4
print("la suma es de:",(num1+num2))
print("la resta es de:",(num1-num2))
print("la multiplicacion es de:",(num1*num2))
print("la divicion es de:",(num1/num2))
print("la divicion exacta es de:",(num1//num2))
print("la potencia es de:",(num1**num2))

#Concatenacion de python

texto1 = "hola"
texto2 = "mundo"

textoFinal = texto1 + " " + texto2
print(textoFinal)
print("El saludo es: %s %s" %(texto1,texto2))

saludoFinal = "Saludo {} {}".format(texto1,texto2)
print(saludoFinal)

saludoFinal2 = "Saludo {x} {y}".format(x = texto1, y = texto2)
print(saludoFinal2)