import os

cambio = [0.111, 0.333, 0.555, 0.777, 0.999]
frec = [.111, .222, .333, .444, .555, .666, .777, .888, .999]
k = 0
for j in reversed(cambio):
    for i in range(len(frec)):
        os.system("python deberiahacertarea.py "+str(frec[i])+" "+str(i+1)+" 10 "+str(j)+" "+str(j)+" 10 >> corrida_"+str(k)+"_"+str(i)+".txt")
    k+=1
