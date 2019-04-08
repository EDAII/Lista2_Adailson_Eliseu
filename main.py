from sorts import bubble, insertion_sort, selection_sort
import sys  
import os
import csv
import random
import time 

registers = []
def main():  

    registers_name = read_file_by_name()
    registers_cpf = read_file_by_cpf()

    print("Dados carregados e tratados com sucesso!\n")
    print("O que deseja fazer com o vetor inicial?\n")
    print("1 - Randomizar vetor")
    print("2 - Ordem original do vetor")
    opc = input()
    if(opc == '1'):
        registers_name = random_vector(registers_name)
        registers_cpf = random_vector(registers_cpf)
    print("Qual ordenação deseja fazer?")
    print("1 - Selection Sort")
    print("2 - Insertion Sort")
    print("3 - Bubble Sort")
    opc = input()

    if(opc == '1'):
        print("Ordenar pelo nome ou pelo CPF?")
        print("1 - Nome")
        print("2 - CPF")
        opc = int(input())
        if(opc == 1):
            start = time.time()
            registers_sorted = selection_sort(registers_name)
            end = time.time()
            elapsed_time = end - start
            sucess_menu(elapsed_time,registers_sorted)
        elif (opc == 2):
            start = time.time()
            registers_sorted = selection_sort(registers_cpf)
            end = time.time()
            elapsed_time = end - start
            sucess_menu(elapsed_time,registers_sorted)
        else:
            print("Fim")
            return
    elif(opc == '2'):
        print("Ordenar pelo nome ou pelo CPF?")
        print("1 - Nome")
        print("2 - CPF")
        opc = int(input())
        if(opc == 1):
            start = time.time()
            registers_sorted = insertion_sort(registers_name)
            end = time.time()
            elapsed_time = end - start
            sucess_menu(elapsed_time,registers_sorted)
        elif(opc == 2):
            start = time.time()
            registers_sorted = insertion_sort(registers_cpf)
            end = time.time()
            elapsed_time = end - start
            sucess_menu(elapsed_time,registers_sorted)
        else:
            print("Fim")
            return
    elif(opc == '3'):
        print("Ordenar pelo nome ou pelo CPF?")
        print("1 - Nome")
        print("2 - CPF")
        opc = int(input())
        if(opc == 1):
            start = time.time()
            registers_sorted = bubble(registers_name)
            end = time.time()
            elapsed_time = end - start
            sucess_menu(elapsed_time,registers_sorted)
        elif(opc == 2):
            start = time.time()
            registers_sorted = bubble(registers_cpf)
            end = time.time()
            elapsed_time = end - start
            sucess_menu(elapsed_time,registers_sorted)
        else:
            print("Fim")
            return
    
def read_file_by_name():
    filepath = 'registered0.csv'
    registers = []
    if not os.path.isfile(filepath):
       print("O Arquivo {} não foi encontrado.".format(filepath))
       sys.exit()

    with open(filepath) as fp:
       for line in fp:
           # Tratamento para formato nome completo
           line = line.replace('"','',len(line))
           line = line.split(',') 
           line = (line[1][1:] + line[2] + line[3][:-1])
           registers.append(line)

    return registers

def read_file_by_cpf():
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
           line = (line[0])
           registers.append(line)
           print("Linha {} contém {}".format(cnt, line))
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

def sucess_menu(elapsed_time, registers_sorted):
    print('Ordenado com sucesso!')
    print('Tempo para realizar ordenação: ', elapsed_time)
    print('Deseja mostrar lista ordenada?')
    print("1 - Sim")
    print("2 - Não")
    opc = int(input())
    if(opc == 1):
        print(registers_sorted)
    else:
        print("Fim")
        return
main()