import random 
from sort import select_sort, dubble_sort, insertion_sort, merge_sort, quicksort

any_numbers = random.sample(range(1,1000), 42)

already_sort = [1,2,3,4,5,6,9,20,22,23,28,32,34,39,40,42,76,87,99,112]

inversed = [117,90,88,83,81,77,74,69,64,63,51,50,49,42,41,34,32,29,28,22,16,8,6,5,3,1]

repeated = [7,7,7,7,7,1,1,9,9,2,4,4,4,5,4,5,7,1]

number = [3, 20, 6, 4, 50, 55, 1, 8, 20, 11]

if __name__ == "__main__":
        test_class = {
            'Números eleatórios': any_numbers,
            'Já ordenados': already_sort,
            'Ordem Inversa': inversed,
            'Elementos repetidos': repeated,
            'Listando number': number
        }

        print("********************************")
        for name, lista in test_class.items():
            print("\n Caso de teste: {}".format(name))
            print(lista)
            merge_sort(lista)
            print("\n Ordenado:")
            print(lista)

