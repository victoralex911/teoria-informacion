import os

for i in range (1,1000):
    os.system("python stringmatch.py bf "+str(i)+" >> Bruteforce.txt")

for i in range (1,1000):
    os.system("python stringmatch.py kmp "+str(i)+" >> KMP.txt")
