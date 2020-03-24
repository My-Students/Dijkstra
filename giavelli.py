inf=1000
grafo = [0,1,2,3]
distance=[0,inf,inf,inf] 
matrix =[[0, 1, 4, 0],[1, 0, 1, 3],[4, 1, 0, 1],[0, 3, 1, 0]]
while len(grafo)>0:
    nodo=grafo[0]
    grafo.pop(0)
    distance.pop(0)
    min=100
    vicini=[]
    k=0
    for k in matrix:
        if (matrix[k][nodo] != 0):
            vicini.append(matrix[k][nodo])
            if(vicini[k]<distance[k] & (nodo==0)):
                distance[k]=vicini[k]
            if(vicini[k]<distance[k]):
                for h in vicini:
                    dist=[]
                    if((distance[0]+vicini[h])<distance[1]):
                        dist.append(distance[0]+vicini[h])
                distance=dist
percorso = min(distance)
print(percorso)
    
