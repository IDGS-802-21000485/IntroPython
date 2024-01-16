num1 = 10
num2 = 0

try:
    resultado= num1/num2
    print(resultado)
except ZeroDivisionError:
    print("Error en el programa---------------------")
finally:
    print("Yo siempre aparezco")