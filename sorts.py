def selection_sort(lista):
    for count in range(len(lista)):
        index = count
        for count2 in range(count+1, len(lista)):
            if lista[count2] < lista[index]:
                index = count2
        if index != count:
            aux = lista[index]
            lista[index] = lista[count]
            lista[count] = aux

    return lista

def insertion_sort(lista):
    for count in range(1, len(lista)):
        chave = lista[count]

        aux = count-1
        while (aux > -1) and chave < lista[aux]:
            lista[aux+1] = lista[aux]
            aux = aux-1
        lista[aux+1] = chave

    return lista

def bubble(lista):
    flag = True
    while (flag):
        flag = False
        for count in range(0, len(lista)-1):
            if lista[count] > lista[count+1]:
                aux = lista[count]
                lista[count] = lista[count+1]
                lista[count+1] = aux
                flag = True

    return lista
