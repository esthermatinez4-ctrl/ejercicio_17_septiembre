def ordenar_por_insercion(lista):
    for i in range(1, len(lista)):
        elemento = lista[i]
        posicion = i - 1

        while posicion >= 0 and lista[posicion] > elemento:
            lista[posicion + 1] = lista[posicion]
            posicion -= 1

        lista[posicion + 1] = elemento

    return lista

lista = [7, 2, 9, 4, 1, 6]
print("Lista original:", lista)
print("Lista ordenada:", ordenar_por_insercion(lista))