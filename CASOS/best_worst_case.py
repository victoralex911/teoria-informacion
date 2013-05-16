from random import shuffle, random, choice
from sys import argv

lista = "abcdefghijklmnopqrstuvwxyz"

def peor(nombre, rango):
    for j in range(10):
        PEOR = ""
        peor = []
        for char in lista:
            for i in range(rango):
                peor.append(char)
        shuffle(peor, random)
        for char in peor:
            PEOR+=char
        file = open(nombre+"_"+str(j)+".txt", "w")
        file.write(PEOR)
        file.close()

def tipico(nombre, rango):
    for j in range(10):
        TIPICO = ""
        for i in range(len(lista)):
            for j in range(rango):
                TIPICO += choice(lista)
        file = open(nombre+"_"+str(j)+".txt", "w")
        file.write(TIPICO)
        file.close()

for i in range(int(argv[1])):
    iter = int(argv[2])
    tipico("TIPICO_"+str(i), iter)
    iter = iter**2
