
lista = [3,5,7,1,8]

def select_sort(lista):
    n = len(lista)
    for j in range(n-1):
        min_index = lista[0]
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux