from sorts import bubble, insertion_sort, selection_sort
import sys  
import os
import csv

registers = []
def main():  
    
    print("Qual ordenação deseja fazer?")
    print("1 - Selection Sort")
    print("2 - Insertion Sort")
    print("3 - Bubble Sort")
    opc = input()

    if(opc == '1'):
        print(selection_sort(read_file()))
    elif(opc == '2'):
        print(insertion_sort(read_file()))
    elif(opc == '3'):
        print(bubble(read_file()))
    
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

main()