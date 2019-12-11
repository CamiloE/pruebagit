import random
import numpy as np
#Calculo de probabilidades
def probabilidades(ph,ben,n,alfa,beta):
    total=0
    for a in range(0,N):
        temp=(ph[a]**alfa)*(ben[a]**beta)
        total += temp
    probabilidades=[(((ph[b]**alfa)*(ben[b]**beta))/total) for b in range(0,N)]
    #com=[]
    total=0
    com=np.cumsum(probabilidades)
    com=list(com)
    total=0
    return com
#################################################
N=100#Numero de Bloques
c=15#capacidad de la mochila
ants=20#numero de hormigas
alfa=2
beta=4
n_list=np.arange(1,101,1)#listado de bloques
pesos=np.array([5,5,2,4,2,2,3,4,5,1,4,5,4,5,1,5,3,3,5,4,1,3,5,3,3,4,1,3,2,5,2,3,4,4,2,5,1,3,2,4,3,3,2,4,1,1,5,3,3,5,1,2,3,3,2,1,3,3,4,5,1,3,3,5,3,3,1,4,4,4,5,1,2,3,1,3,2,2,5,5,5,3,4,1,5,1,2,5,2,1,1,2,3,1,1,5,1,5,3,5])#Pesos de cada bloque
minimo=np.amin(pesos)#peso minimo del listado
ferormona=0.1*np.ones(N)#cantidad inicial de ferormona en cada bloque
costo=np.array([3,8,2,8,5,8,9,2,3,1,9,1,3,6,7,10,4,4,4,2,3,9,10,2,8,2,1,8,6,2,9,8,8,7,3,2,8,5,3,7,9,1,1,6,5,4,9,6,10,7,8,8,7,3,4,6,3,9,9,9,3,3,8,4,2,10,3,10,4,4,6,2,8,4,6,2,8,7,10,2,9,3,5,5,3,6,9,2,9,4,10,1,4,1,2,5,5,7,10,3])#costo de cada bloque
beneficio=(1/10)*costo#arreglo con el beneficio de cada bloque
trayectorias=[]#almacena la trayectoria realizada por cada hormiga
for z in range(0,5):#ciclo para las iteraciones de todas las hormigas
    compuertas=probabilidades(ferormona,beneficio,N,alfa,beta)#invocar la funcion para calcular la probabilidad
    trayectorias.clear()#vacia las trayectorias
    ganancias=np.empty(0,int)#array para almacenar la ganancia de cada hormiga
    ##creacion de la trayectoria
    for k in range(0,ants):#ciclo para que todas las hormigas realicen el recorrido
        cdisponible=c#capacidad disponible de la mochila
        camino_ant=np.empty(0,int)#array que almacena el recorrido de la hormiga
        ganancia=0#variable para almacenar la ganancia de cada hormiga
        while cdisponible>minimo:#bucle para realizar el llenado de la mochila hasta que no haya espacio
            select=random.random()#escoge numero aleatorio entre 0 y 1
            #Seleccion del ladrillo
            for i in range(0,N):#la hormiga visualiza y compara todos los bloques
                if select<=compuertas[i]:
                    bloque=i+1
                    if bloque not in camino_ant:#condicional para ver si el bloque seleccionado no esta aun en el recorrido
                        if((cdisponible-pesos[i])<=0):#verifica que con el bloque seleccionado sobrepase la capacidad
                            break
                        else:
                            camino_ant=np.append(camino_ant,bloque)#añade al array de recorrido el bloque seleccionado
                            cdisponible -=pesos[i]#reduce la capacidad disponible de la mochila
                            ganancia += costo[i]#incrementa el costo transportado
                            break
                    else:
                        select=random.random()#seleccciona numero aleatorio si el bloque seleccionado ya esta en la ruta
                        i=0
        trayectorias.append(camino_ant)#añade el camino de cada hormiga en forma de matriz
        ganancias=np.append(ganancias,ganancia)#añade la ganancia de cada hormiga
    solution=np.amax(ganancias)#se selecciona la hormiga  con la mejor ganancia
    solution_way=trayectorias[list(ganancias).index(solution)]#lista de bloques recorrido por la mejor hormiga
    for block in n_list:
        if block in solution_way:#refuerzo de la feromona
            ferormona[block-1] = 0.9*ferormona[block-1]+beneficio[block-1]
        else: #evaporacion de la feromona
            ferormona[block-1] = 0.9*ferormona[block-1]