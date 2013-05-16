import os

for i in [1,2,3,4,5,10,20,30,40,50,100,200,300,400,500,1000,2000,3000,4000,5000,10000]:
        os.system("python huffman_ada.py Texto.txt "+str(i)+" adap >> ada.txt")

os.system("python huffman.py Texto.txt >> normal.txt")
