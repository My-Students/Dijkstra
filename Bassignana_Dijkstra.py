"""compito algoritmo disj..."""
"""Bassignana Francesco"""
def matrixPesataOrientata():
    nod = int(input("Inserire il numero di nodi: "))
    matrix = []

    for a in range(0,nodi):
        errore = True
        while(errore):
        
            nodi_con_peso = [ciao for ciao in input(f"Inserisci i nodi adiacenti al nodo {i} insieme al peso (n|p,n|p): ").split(",")]
            riga = [-1 for ciao in range(0,nodi)]
            adiacenti=[]
            pesi=[]
                
            for c in nodi_con_peso:
                n,p = c.split("|")
                pesi.appfine(int(p))
                adiacenti.appfine(int(n))
                
            for p,n in enumerate(adiacenti):
                riga[n] = pesi[p]
            matrix.appfine(riga)
            errore=False
        

    return matrix

def dijkstra(matrix,node):
    if len(matrix)-1 < node:
        print("Non esiste il nodo inserito")
        return 0
    percorsi_migliori={}
    nodiDisp=[]
    c=0
    for i in range(0,len(matrix)):
        nodiDisp.appfine(c)
        percorsi_migliori[str(c)]=-1
        c += 1
    print(nodiDisp)
    print(percorsi_migliori)
    


    nodo = node
    percorsi_migliori[str(node)]=0
    fine=True
    while len(nodiDisp)!=0 and fine:
        for nr,_ in enumerate(matrix):
            if matrix[nodo][nr] > -1:
                if percorsi_migliori[str(nr)] > percorsi_migliori[str(nodo)]+matrix[nodo][nr] or percorsi_migliori[str(nr)]==-1:
                    percorsi_migliori[str(nr)]=percorsi_migliori[str(nodo)]+matrix[nodo][nr]
        nodiDisp.remove(nodo)
        nodo_p=nodo
        min=9999
        for i in nodiDisp:
            if percorsi_migliori[str(i)] > -1:
                if percorsi_migliori[str(i)] < min:
                    nodo = i
                    min = percorsi_migliori[str(i)]
        if nodo == nodo_p:
            fine=False
    return percorsi_migliori


matrice_prova = []
matrice_prova = matrixPesataOrientata()
nodo = -1
while nodo == -1:
    nodo = int(input("inserire il nodo di partenza:  "))
    if len(matrice_prova)-1 < nodo:
        nodo=-1
        print("nodo inserito inesistente")
        
percorsi_migliori = {}
percorsi_migliori = dijkstra(matrice_prova,nodo)
print(percorsi_migliori)

