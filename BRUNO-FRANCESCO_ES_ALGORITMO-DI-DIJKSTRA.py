def creaMatrice():
    v = int(input("Inserire numero nodi: "))
    matrix = []
    for i in range(1, v + 1):
        e = [int(i) for i in input(f"Inserire le vicinanze del nodo {i} (usare la '.' come separatore): ").split('.')]
        colonna = [0 for dim in range(0, v)]
        for j in e:
            if j != i:
                colonna[j - 1] = int(input(f"Inserire il peso tra il nodo {i} e il nodo {j}"))
        matrix.append(colonna)

    return matrix


def stampaMatrice(matrix):
    for r in range(0, len(matrix)):
        print(" ")
        for c in range(0, len(matrix)):
            print(matrix[r][c], end=' ')


def stampaDict(dict):
    for key, val in dict.items():
        if key == "precedente":
            print(f"{key}: {val}")
        else:
            print(f"{key}: \t\t{val}")


def dijkstra(matrix):
    source = int(input("\nInserisci il nodo sorgente: "))
    usati = {"nodi": [], "pesi": [], "precedente": []}
    dist = [100000000 for _ in range(0, len(matrix))]
    dist[source] = 0
    successori = [i for i in range(0, len(matrix))]
    prec = source
    while len(successori) > 0:
        u = min(dist)
        nodo = successori.pop(dist.index(u))
        dist.remove(u)
        usati["nodi"].append(nodo)
        usati["pesi"].append(u)
        usati["precedente"].append(prec)
        for nodiVicini in matrix[nodo]:
            if nodiVicini > 0 and matrix[nodo].index(nodiVicini) in successori:
                # matrix[nodo].index(nodiVicini) --> posizione nella matrice
                # successori.index(matrix[nodo].index(nodiVicini)) --> posizione nodo in successori
                # nodiVicini + u --> nuova distanza
                if nodiVicini + u < dist[successori.index(matrix[nodo].index(nodiVicini))]:
                    dist[successori.index(matrix[nodo].index(nodiVicini))] = nodiVicini + u
            matrix[nodo][matrix[nodo].index(nodiVicini)] = 0
        prec = nodo
    return usati


def main():
    grid = [[0, 1, 4, 0],
            [1, 0, 1, 3],
            [4, 1, 0, 1],
            [0, 3, 1, 0]]
    stampaMatrice(grid)
    stampaDict(dijkstra(grid))


if __name__ == '__main__':
    main()
