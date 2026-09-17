a = int(input("Introduce el dividendo: "))
b = int(input("Introduce el divisor: "))

cociente = 0
resto = a

while resto >= b:
    resto = resto - b
    cociente = cociente + 1

print("Cociente:", cociente)
print("Resto:", resto)