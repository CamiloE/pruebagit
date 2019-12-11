import random
import numpy as np
#Calculo de probabilidades
def probabilidades(ph,ben,n):
    total=0
    probabilidades=[]
    for a in range(0,N):
        temp=ph[a]*ben[a]
        total += temp
    for b in range(0,N):
        p=(ph[b]*ben[b])/total
        probabilidades.append(p)
    com=[]
    total=0
    for j in range(0,N):
        total +=probabilidades[j]
        com.append(total)
    total=0
    return com
#################################################
N=int(input("Ingresa el numero de cantidad de bloques para el problema: "))
c=int(input("Ingresa la capacidad para la mochila: "))
ants=int(input("Ingrese el numero de Hormigas que hay en la colonia: "))
n_list=np.arange(1,N+1,1)
pesos=np.random.randint(1,c/2,size=N)
minimo=np.amin(pesos)
ferormona=0.1*np.ones(N)
costo=np.random.randint(1,10,size=N)
beneficio=(1/10)*costo
compuertas=probabilidades(ferormona,beneficio,N)
trayectorias=[]
##creacion de la trayectoria
for k in range(0,ants):
    cdisponible=c
    camino_ant=[]
    while cdisponible>minimo:
        select=random.random()
        #Seleccion del ladrillo
        for i in range(0,N):
            if select<=compuertas[i]:
                bloque=i+1
                if bloque not in camino_ant:
                    if((cdisponible-pesos[i])<=0):
                        break
                    else:
                        camino_ant.append(bloque)
                        cdisponible -=pesos[i]
                        break
                else:
                    select=random.random()
                    i=0
    trayectorias.append(camino_ant)