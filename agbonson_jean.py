def dijkstra(matrix)-> dict:
    source = int(input("\nInserisci il nodo sorgente: "))
    used = {"nodes": [], "weights": [], "previous": []}
    distance = [100000000 for _ in range(0, len(matrix))]
    distance[source] = 0
    following = [i for i in range(0, len(matrix))]
    prec = source
    while len(following) > 0:
        distance_min = min(distance)
        nodo = following.pop(distance.index(distance_min))
        distance.remove(distance_min)
        used["nodes"].append(nodo)
        used["weights"].append(distance_min)
        used["previous"].append(prec)
        for nodes_Near in matrix[nodo]:
            if nodes_Near > 0 and matrix[nodo].index(nodes_Near) in following:
                if nodes_Near + distance_min < distance[following.index(matrix[nodo].index(nodes_Near))]:
                    distance[following.index(matrix[nodo].index(nodes_Near))] = nodes_Near + distance_min
            matrix[nodo][matrix[nodo].index(nodes_Near)] = 0
        prec = nodo
    return used


def main():
    matrix =[[0, 1, 4, 0],
            [1, 0, 1, 3],
            [4, 1, 0, 1],
            [0, 3, 1, 0]]

    dict_dij = dijkstra(matrix)
    print(dict_dij)



if __name__ == "__main__":
    main()