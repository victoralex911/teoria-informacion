import random
from sys import argv

def generar(porcent, largo, numpal):
    palabras = []
    nuevas = []
    x = 0
    while x < numpal:
        palabra=""
        for i in range((largo+1)**2):
            if random.random() < porcent:
                palabra+="0"
            else:
                palabra+="1"
        palabras.append(palabra)
        x+=1
    for i in range(len(palabras)):
        nuevas.append(transmicion(palabras[i], float(argv[4]), float(argv[5])))
        #print palabras[i]
    #print "Transmitiendo..."
    k=0
    for i in nuevas:
        error = 0
        for j in i:
            if j != palabras[k]:
                #print j, "es diferente de ", palabras[k]
                error+=1
        k+=1
        print largo, porcent, error * .1

def transmicion(palabra, cero, uno):
    nueva = []
    x = 0
    while x< int(argv[6]):
        npal=""
        for caracter in palabra:
            if caracter == "0":
                if random.random()<=cero:
                    npal+="0"
                else:
                    npal+="1"
            if caracter == "1":
                if random.random()<=uno:
                    npal+="1"
                else:
                    npal+="0"
        nueva.append(npal)
        x+=1
    return nueva

if len(argv)!=7:
    print "1 - Porcentaje 0 y 1"
    print "2 - Largo de palabra"
    print "3 - Numero de palabras"
    print "4 - Probabilidad de que 0 se quede como 0"
    print "5 - Probabilidad de que 1 se quede como 1"
    print "6 - Repeticiones por palabra"
else:
    generar(float(argv[1]), int(argv[2]), int(argv[3]))
