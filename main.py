from sorts import bubble, insertion_sort, selection_sort
import sys  
import os
import csv
import random

registers = []
def main():  

    registers = read_file()

    print("Dados carregados e tratados com sucesso!\n")
    print("O que deseja fazer com o vetor inicial?\n")
    print("1 - Randomizar vetor")
    print("2 - Ordem original do vetor")
    opc = input()
    if(opc == '1'):
        registers = random_vector(registers)

    print("Qual ordenação deseja fazer?")
    print("1 - Selection Sort")
    print("2 - Insertion Sort")
    print("3 - Bubble Sort")
    
    opc = input()

    if(opc == '1'):
        print(selection_sort(registers))
    elif(opc == '2'):
        print(insertion_sort(registers))
    elif(opc == '3'):
        print(bubble(registers))
    
def read_file():
    filepath = 'registered0.csv'
    registers = []
    if not os.path.isfile(filepath):
       print("O Arquivo {} não foi encontrado.".format(filepath))
       sys.exit()

    with open(filepath) as fp:
       cnt = 0
       for line in fp:
           # Tratamento para formato nome completo
           line = line.replace('"','',len(line))
           line = line.split(',') 
           line = (line[1][1:] + line[2] + line[3][:-1])
           registers.append(line)
           #print("Linha {} contém {}".format(cnt, line))
           cnt += 1
    
    return registers

def random_vector(lista):
    tmp_regs = read_file()
    lista = []
    for count in tmp_regs:
        choice = random.choice(tmp_regs)
        if(lista.index != choice):
            lista.append(choice)
        else:
            lista.append(random.choice(tmp_regs))
    return lista

main()