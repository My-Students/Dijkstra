def dict2adj(d):
    m = []
    l = [False for i in range(0,len(d))]
    for k, e in d.items():
        for i in e:
            l[i-1] = 1
        m.append(l)
    return m

def matrix2dict(matrix):
    number_of_nodes = 1
    for i in range(0,len(matrix)):
        for e in range(0,len(matrix)):
            if matrix[i][e]:
                matrix[i][e] = number_of_nodes
                number_of_nodes = number_of_nodes + 1
    d = {}
    offset = 1
    number_of_nodes= 1
    links =[]

    for r in range(0,len(matrix)):
        for e in range(0,len(matrix)):
            links= []
            if matrix[r][e]!= False:
                if r-offset >= 0:
                    if(matrix[r-offset][e]!=False):
                        links.append(matrix[r-offset][e])

                if e-offset >= 0:
                    if(matrix[r][e-offset]!=False):
                        links.append(matrix[r][e-offset])

                if e+offset < len(matrix):
                    if(matrix[r][e+offset]!=False):
                        links.append(matrix[r][e+offset])

                if r+offset < len(matrix):
                    if(matrix[r+offset][e]!=False):
                        links.append(matrix[r+offset][e])

                d[number_of_nodes] = links
                number_of_nodes =number_of_nodes+1
    return d

def matrix2HevayDict(matrix):
    number_of_nodes = 1
    for i in range(0,len(matrix)):
        for e in range(0,len(matrix)):
            if matrix[i][e]:
                matrix[i][e] = number_of_nodes
                number_of_nodes = number_of_nodes + 1
    d = {}
    offset = 1
    number_of_nodes= 1
    links =[]

    for r in range(0,len(matrix)):
        for e in range(0,len(matrix)):
            links= []
            if matrix[r][e]!= False:
                if r-offset >= 0:
                    if(matrix[r-offset][e]!=False):
                        links.append(matrix[r-offset][e])

                if e-offset >= 0:
                    if(matrix[r][e-offset]!=False):
                        links.append(matrix[r][e-offset])

                if e+offset < len(matrix):
                    if(matrix[r][e+offset]!=False):
                        links.append(matrix[r][e+offset])

                if r+offset < len(matrix):
                    if(matrix[r+offset][e]!=False):
                        links.append(matrix[r+offset][e])
                p = len(links)
                for _ in range(0,p):
                    links.append(1)
                d[number_of_nodes] = links
                number_of_nodes =number_of_nodes+1
    return d

def dijkstra(d, source_node):
    #define max distance to assing as infinite
    q = []  #saves all nodes
    prev = []
    max_dist = 0
    for k,v in d.items():
        q.append(k)
        for i in v[int(len(v)/2):]:
            max_dist = max_dist + i#calculate max distance
        prev.append(None)
    dist = [int(max_dist*2) for _ in q]
    dist[source_node-1] = 0
    while len(q) > 0:
        u = q[dist.index(min(dist))]
        #print("================")
        #print(dist)
        #print(q)
        #print(f"u = {u}")
        #print(q.index(u))
        q.pop(q.index(u))   #find u and pop from the list

        #print(len(d[u])/2)
        neighbor = d[u][:(int)(len(d[u])/2)] #search neighbors
        #print(f"vicini = {neighbor}")
        for k,v in enumerate(neighbor):
            #print(f"k = {k} v = {v} ")
            #print(dist[u-1])
            #print(d[u][k+int(len(d[u])/2)])
            alt = dist[u-1] + d[u][k+int(len(d[u])/2)]
            #print(alt)
            #print(v-1)
            if alt < dist[v-1]:
                #print("cambio")
                dist[v-1] = alt
                #print(f"v-1 = {v-1}")
                prev[v-1] = u-1
            #print(dist)

    return dist, prev

def main():
    grid = [[True, True, True, True, True, False],
            [False, False, True, True, True, False],
            [True, True, True, False, True, True],
            [True, False, False, True, True, False],
            [True, True, True, True, False, True],
            [True, False, True, True, True, False]]


    dictionary = matrix2HevayDict(grid)
    dist, prev = dijkstra(dictionary,1)
    print(f"dist = {dist} prev = {prev}")


if __name__ == "__main__":
    main()
