def main():
    matrice = []
    matrice = new_grafo_no_oriented_weighted() #riga = nodo corrente dove ogni cella contiene il valore del collegamento tra il nodo (riga) e un altro nodo (colonna), 0 se non sono collegati
    nodo = -1
    while nodo == -1:
        nodo = int(input("Inserire il nodo su cui applicare djkstra: "))
        if nodo > len(matrice)-1 or nodo < 0:
            print("Nodo insesistente")
            nodo=-1
    percorsi = {}
    percorsi = dijkstra(matrice,nodo)
    print(percorsi)
    

def new_grafo_no_oriented_weighted():
    nodi = int(input('Inserisci il numero di nodi: '))
    matrix = []
    for k in range(0, nodi):
        lista = [int(n) for n in input(f"Quali sono i nodi vicini al nodo {k}? \t").split(",")]
        colonne = [0 for n in range(0,nodi)]
        for n in lista:
            if(n != -1):
                colonne[n] = input(f"Inserisci il peso del collegamento tra il nodo {k} e il nodo {n}: ")
        matrix.append(colonne)
    print(matrix)
    return matrix


def dijkstra(matrice,nodo):
    lista = {"nodes": [], "weights": [], "precedente": []}
    dist = [1000000 for k in range(0, len(matrice))]
    dist[nodo] = 0
    successori = [k for k in range(0, len(matrice))]
    pre = nodo
    while len(successori) > 0:
        minimo = min(dist) #min è una funzione che cerca il valore minimo in dist
        node = successori.pop(dist.index(minimo))
        dist.remove(minimo)
        lista["nodes"].append(node)
        lista["weights"].append(minimo)
        lista["precedente"].append(pre)
        for adiacenti in matrice[node]:
            if adiacenti > 0 and matrice[node].index(adiacenti) in successori:
                if adiacenti + minimo < dist[successori.index(matrice[node].index(adiacenti))]:
                    dist[successori.index(matrice[node].index(adiacenti))] = adiacenti + minimo
            matrice[node][matrice[node].index(adiacenti)] = 0
        pre = node
    return lista
    
if __name__ == "__main__":
    main()