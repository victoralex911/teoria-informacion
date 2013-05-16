import numpy as np
from random import randint

def hamming(palabra):
    d = []
    lista = []
    for bit in palabra:
        lista.append(int(bit))
    d.append(lista)
    d = np.matrix(d)
    G = np.matrix([[1,0,0,0,0,1,1],[0,1,0,0,1,0,1],[0,0,1,0,1,1,0],[0,0,0,1,1,1,1]])
    P = d*G
    Pal = []
    for R in P:
        for E in R:
            Pal = E%2
    return Pal

def decode(p):
    palabra = str(p[0][0])+str(p[0][1])+str(p[0][2])+str(p[0][3])
    return palabra

def correct(p, n):
    if p[0][n-1] == 0:
        p[0][n-1] = 1
    else:
        p[0][n-1] = 0
    return p

def check(palabra):
    H = np.matrix([[0,0,0,1,1,1,1],[0,1,1,0,0,1,1],[1,0,1,0,1,0,1]])
    syndrome = H*np.transpose(palabra)
    syndrome = syndrome.tolist()
    c_bits=""
    for row in syndrome:
        for n in row:
            c_bits+=str(int(n)%2)
    return int(c_bits, 2)

file = open("quijote.txt", "r")
palabra =file.read()
lista = []
for char in palabra:
    lista.append(str(bin(ord(char))))

for i in range(len(lista)):
    zeros = ""
    lista[i]=lista[i][2:]
    if len(lista[i]) != 8:
        for j in range(8-len(lista[i])):
            zeros+="0"
        lista[i]=zeros+lista[i]

hl= []
for pal in lista:
    hl.append(hamming(pal[:4]))
    hl.append(hamming(pal[4:]))

n_pal = []
i = 0
for pal in hl:
    n = check(pal)
    if True:
        #print pal[0], "<--Orig"
        x = pal[0].tolist()
        rand = randint(0,6)
        if x[0][rand] == 0:
            x[0][rand] = 1
        else:
            x[0][rand] = 0
        x=np.array(x)
        n1 = check(x)
        if n1 != 0:
            n_pal.append(decode(correct(x.tolist(), n1)))
        else:
            n_pal.append(decode(x.tolist()))
        #print x,"<--Modi en:",rand+1
    elif n != 0:
        n_pal.append(decode(correct(pal[0].tolist(), n)))
    else:
        n_pal.append(decode(pal[0].tolist()))
texto = ""
while i < len(n_pal):
    texto+=chr(int(n_pal[i]+n_pal[i+1],2))
    i+=2
print texto
