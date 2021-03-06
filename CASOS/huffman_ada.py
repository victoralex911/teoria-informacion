import collections
from sys import argv
import time

class Nodo:
    def __init__(self, char, frec):
        self.char = char
        self.frec = frec
        self.nodo_izq = None
        self.nodo_der = None
        self.dir = None

    def hijo_izq(self, nodo_izq):
        self.nodo_izq = nodo_izq

    def hijo_der(self, nodo_der):
        self.nodo_der = nodo_der

def guardar(binario):
    bin = ""
    file = open("binario.txt", "wb")
    for bit in binario:
        bin+=bit
        if len(bin) == 8:
            byte = int(bin, 2)
            file.write("%c" % byte)
            bin = ""
    if bin != "":
        while len(bin) != 8:
            bin+="0"
            byte = int(bin, 2)
        file.write("%c" % byte)
    file.close()

def bin_to_text(binario):
    texto = ""
    saved_bit=""
    for bit in binario:
        try:
            saved_bit += bit
            texto += binarios[saved_bit]
            saved_bit=""
        except:
            pass
    return texto


def ordenar_nodos(nodos):
    ord_nodos = []
    frec_nodos = []
    lista = []
    for nodo in nodos:
        frec_nodos.append(nodo.frec)
        if nodo.char not in lista:
            lista.append(nodo.char)
    new_frec_nodos = sorted(frec_nodos)
    for new_frec in new_frec_nodos:
        for frec in new_frec_nodos:
            for nodo in nodos:
                if nodo.char in lista:
                    if nodo.frec == frec and frec == new_frec:
                        lista.remove(nodo.char)
                        ord_nodos.append(nodo)
    return ord_nodos

def tree(nodos):
    while len(nodos)!=1:
        N = Nodo(nodos[0].char+nodos[1].char, nodos[0].frec+nodos[1].frec)
        nodos[1].dir = "1"
        N.hijo_izq(nodos[1])
        nodos[0].dir = "0"
        N.hijo_der(nodos[0])
        nodos.pop(0)
        nodos.pop(0)
        nodos.append(N)
        nodos = ordenar_nodos(nodos)
    return nodos[0]

def leer():
    file = open("binario.txt", "rb")
    bytes = []
    try:
        byte = file.read(1)
        bytes.append(byte)
        while byte != "":
            byte = file.read(1)
            bytes.append(byte)
    finally:
        file.close()
    bintext = ""
    for byte in bytes:
        try:
            bintext += str("{0:b}".format(ord(byte)))
        except:
            pass
    return bintext

def dividir(palabra, rango):
    palabras = []
    current = ""
    counter = 0
    for char in palabra:
        current += char
        counter += 1
        if counter == rango:
            counter = 0
            palabras.append(current)
            current = ""
    palabras.append(current)
    return palabras

def imprimir(nodo, string):
    string+=nodo.dir
    try:
        imprimir(nodo.nodo_izq, string)
        imprimir(nodo.nodo_der, string)
    except:
        valores.update({nodo.char : string})
        binarios.update({string : nodo.char})

file = open(argv[1], "r")

original = file.read()
nodos = []
count_nodos = []
binarios = {}
valores = {}
tiempo1 = time.time()
listas = dividir(original,int(argv[2]))

#print listas
if argv[3]== "adap":
    for palabra in listas:
        for char in palabra:
            if char not in count_nodos:
                count_nodos.append(char)
                nodos.append(Nodo(char, palabra.count(char)))
                nodos = ordenar_nodos(nodos)
        nodo = tree(nodos)

elif argv[2]=="norm":
    for char in original:
        if char not in count_nodos:
            count_nodos.append(char)
            nodos.append(Nodo(char, original.count(char)))

    nodos = ordenar_nodos(nodos)
    nodo = tree(nodos)


imprimir(nodo.nodo_izq, "")
imprimir(nodo.nodo_der, "")

binario = ""
for char in original:
    binario+=valores[char]
guardar(binario)

texto2 = bin_to_text(binario)
tiempo2 = time.time()
#print original
#print texto2
print argv[2], tiempo2-tiempo1
