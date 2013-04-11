from random import shuffle, random, choice
from sys import argv

lista = "abcdefghijklmnopqrstuvwxyz"

def peor():
    PEOR = ""
    peor = []
    for char in lista:
        for i in range(int(argv[1])):
            peor.append(char)
    shuffle(peor, random)
    for char in peor:
        PEOR+=char
    file = open("PEOR.txt", "w")
    file.write(PEOR)
    file.close()

def tipico():
    TIPICO = ""
    for i in range(len(lista)):
        for j in range(int(argv[1])):
            TIPICO += choice(lista)
    file = open("TIPICO.txt", "w")
    file.write(TIPICO)
    file.close()

peor()
tipico()
