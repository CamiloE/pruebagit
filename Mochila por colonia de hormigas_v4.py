import random
import numpy as np
#Calculo de probabilidades
def probabilidades(ph,ben,n):
    total=0
    for a in range(0,N):
        temp=ph[a]*ben[a]
        total += temp
    probabilidades=[((ph[b]*ben[b])/total) for b in range(0,N)]
    total=0
    com=np.cumsum(probabilidades)
    total=0
    return com
#################################################

c=15
ants=5
n_list=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
pesos=np.array([3,5,1,5,2,1,4,5,5,2,3,4,5,1,2,4,2,1,3,4])
minimo=np.amin(pesos)#peso minimo de los ladrillos
N=len(n_list)
costo=np.array([2,5,3,10,2,8,4,1,1,6,4,10,10,3,7,8,4,8,8,9])
ferormona=0.1*np.ones(N)
beneficio=(1/10)*costo#factor de seleccion relacionado con el costo
trayectorias=[]
#numero de iteraciones de todas las hormigas
for z in range(0,5):# 5 iteraciones totales que hacen las hormigas para encontrar la solucion
    compuertas=probabilidades(ferormona,beneficio,N)#llama la funcion para las probabilidades de cada bloque
    trayectorias.clear()#vacia la matriz de trayectorias
    ganancias=np.empty(0,int)#lista de ganancia correspondiente a cada una de las hormigas
    for k in range(0,ants):#ciclo para que todas las hormigas hagan una trayectoria
        cdisponible=c#capacidad disponible inicial que tendra la mochila
        camino_ant=np.empty(0,int)#lista de bloques escogidos por cada hormiga
        ganancia=0# la ganancia obtenida en el recorrido por cada hormiga
        while cdisponible>minimo:
            select=random.random()#Numero aleatorio entre 0 y 1 para seleccionar el bloque
            #Seleccion del ladrillo
            for i in range(0,N):
                if select<=compuertas[i]:#seleccion de la compuerta
                    bloque=i+1
                    if bloque not in camino_ant:#revisa si el bloque seleccionado de manera aleatoria no se ha escogido
                        if((cdisponible-pesos[i])<=0):#verificar si con el bloque seleccionado se sobre pase la capacidad de la mochila
                            break
                        else:
                            camino_ant=np.append(camino_ant,bloque)
                            cdisponible -=pesos[i]
                            ganancia += costo[i]
                            break
                    else:
                        select=random.random()#volver a escribir numero aleatorio
                        i=0#reinicia la seleccion de bloques
        trayectorias.append(camino_ant)#añadir el camino de cada hormiga a la matriz de trayectorias
        ganancias=np.append(ganancias,ganancia)#llena la lista con la ganancia de cada hormiga
    solution=np.amax(ganancias)#escoge el mayor de las ganancias
    solution_way=trayectorias[list(ganancias).index(solution)]
    for block in n_list:#actualizar la ferormona de cada bloque
        if block in solution_way:#refurza si el bloque fue seleccionado durante la trayectoria
            ferormona[block-1] = 0.9*ferormona[block-1]+beneficio[block-1]
        else: #evapora si no fue sleccionado
            ferormona[block-1] = 0.9*ferormona[block-1]
archivo=open('Resultados2.txt','a')
archivo.write(str(solution))
archivo.write('\n')
archivo.close()