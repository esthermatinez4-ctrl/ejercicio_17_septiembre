def modulo(a, b):
    cociente = a // b
    resultado = a - (cociente * b)
    return resultado


a = int(input("Introduce a: "))
b = int(input("Introduce b: "))

print("El resultado es:", modulo(a, b))