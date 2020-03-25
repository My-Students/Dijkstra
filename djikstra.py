mat = [[0,1,2,0],[1,0,3,1],[2,3,0,2],[0,1,2,0]]
INFINITO = 1000000000000000000000000

def dijkstra (graph, source):
    q = []
    dist = []
    prev = []
    for v,n in enumerate(graph):
        dist[v] = INFINITO
        prev[v] = None
        q.append(v)
    
    dist[source] = 0

    while q != None:

        minn = INFINITO
        for i in len(dist):
            if (dist[i]<minn):
                minn = i
        
        u = [q[minn], dist[minn]]

        q.remove(minn)

        mat = neighbor(graph, minn)

        for v,m in enumerate(mat):
            alt = dist[minn] + mat[v]
            if (alt < dist[v]):
                dist[v] = alt
                prev[v] = minn
    
    return dist, prev

def neighbor(graph, index):
    matN = []
    for i, c in graph:
        if (c == index):
            matN.append(graph[i][c])
    return matN

def main():
    indice = int(input("inserisci un nodo del grafo da cui partire"))
    print(dijkstra(mat, indice))

if __name__ == "main":
    main()