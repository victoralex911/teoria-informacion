import time
from random import randint
from sys import argv

palabra = "123"
caracteres = ["0","1","2","3","4","5","6","7","8","9"]
texto = ""
for i in range (int(argv[2])):
	texto+=caracteres[randint(0,9)]
def bruteforce():
	print "BRUTEFORCE"
	inicio = time.time()
	match = []
	for i in range(len(texto)):
		matching = 0
		for j in range(len(palabra)):
			if palabra[j] == texto[j+i]:
				matching +=1
				if matching == len(palabra):
					match.append(i)
					break
			else:
				break
			if j==len(texto):
				break
	final = time.time()-inicio
	print argv[2],final
	print "Matching at", match

def kmp():
	print "KMP"
	inicio = time.time()
	char = palabra[0]
	pos = []
	for i in range(len(texto)):
		if texto[i] == char:
			pos.append(i)
	print "List of possible matches:",pos
	match=[]
	for i in range(len(pos)):
		j=pos[i]
		matching = 0
		for char in palabra:
			if char == texto[j]:
				matching +=1
				j+=1
				if matching == len(palabra):
					match.append(pos[i])
					break
			else:
		       		break
			if j==len(texto):
				break
        final = time.time() - inicio
	print argv[2],final
	print "Matching at", match
if argv[1]=="kmp":
	kmp()
if argv[1]=="bf":
	bruteforce()
