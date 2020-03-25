mat= [[0,1,2,0],[1,0,3,1],[2,3,0,2],[0,1,2,0]]
INFI = 100000
def Dijkstra(matr, source):
    Q = []
    dist = []
    prev = []
    for v,n in enumerate(matr):
        dist[v]=INFI
        prev[v]= None
        Q.append(v)
    dist[source] = 0
    while Q != None:
        minn = INFI
        for i in dist:
            if(dist[i]<minn):
                minn = i                
        u = [dist[minn], prev[minn]]
        Q.remove(minn)
        neigh = neighbor(matr, minn)
        for v,m in enumerate(neigh):
            alt = dist[minn] + mat[v]
            if alt<dist[v]:
                dist[v] = alt
                prev[v] = minn
    return dist, prev
def neighbor(mat, indice):
    matNeigh = []
    for i,c in mat:
        if (mat[i][c] == indice):
            matNeigh.append(mat[i][c])
    return matNeigh
def main():
    print(Dijkstra(mat, int(input("inserisci il nodo di partenza"))))
if __name__ =="__main__":
    main()