"""compito algoritmo dijkstra"""
"""Gabutti Irene"""
def MOrientPes():
    m = []
    nodes = int(input("Inserire il numero di nodi: "))
    

    for a in range(0,nodes):
        error = True
        while(error):
        
            nodes_peso = [y for y in input(f"Inserisci i nodi adiacenti al nodo {a} insieme al peso (n|p,n|p): ").split(",")]
            riga = [-1 for y in range(0,nodes)]
            pesi =[]           
            adiacenti=[]
            
                
            for c in nodes_peso:
                n,p = c.split("|")
                pesi.append(int(p))
                adiacenti.append(int(n))
                
            for p,n in enumerate(adiacenti):
                riga[n] = pesi[p]
            m.append(riga)
            error=False
        

    return m

def algoritmo(m,node):
    if len(m)-1 < node:
        print("Non esiste il nodo inserito")
        return 0
    percorsi_migliori={}
    nodiDisponibili=[]
    c=0
    for i in range(0,len(m)):
        nodiDisponibili.append(c)
        percorsi_migliori[str(c)]=-1
        c += 1
    print(nodiDisponibili)
    print(percorsi_migliori)
    


    nodo=node
    percorsi_migliori[str(node)]=0
    fine=True
    while len(nodiDisponibili)!=0 and fine:
        for nr,_ in enumerate(m):
            if m[nodo][nr] > -1:
                if percorsi_migliori[str(nr)] > percorsi_migliori[str(nodo)]+m[nodo][nr] or percorsi_migliori[str(nr)]==-1:
                    percorsi_migliori[str(nr)]=percorsi_migliori[str(nodo)]+m[nodo][nr]
        nodiDisponibili.remove(nodo)
        nodo_p=nodo
        min=9999999
        for i in nodiDisponibili:
            if percorsi_migliori[str(i)] > -1:
                if percorsi_migliori[str(i)] < min:
                    nodo = i
                    min = percorsi_migliori[str(i)]
        if nodo == nodo_p:
            fine=False
    return percorsi_migliori


matrice_prova = []
matrice_prova = MOrientPes()
nodo = -1
while nodo == -1:
    nodo = int(input("inserire il nodo di partenza:  "))
    if len(matrice_prova)-1 < nodo:
        nodo=-1
        print("nodo inserito inesistente")
        
percorsi_migliori = {}
percorsi_migliori = algoritmo(matrice_prova,nodo)
print(percorsi_migliori)

