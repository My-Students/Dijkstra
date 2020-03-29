"""
dijkstra 
"""

def MatricePesataOrientata():
    nodi = int(input("Inserire numero di nodi: "))
    matrice = []

    for i in range(0,nodi):
        error = True
        while(error):
            try:
                nodi_pesati = [elemento for elemento in input(f"Inserisci gli eventuali nodi adiacenti al nodo {i} con il peso (nodo|peso,nodo|peso): ").split(",")]
                riga = [-1 for elemento in range(0,nodi)]
                nodi_vicini=[]
                pesi=[]
                    
                for c in nodi_pesati:
                    n,p = c.split("|")
                    nodi_vicini.append(int(n))
                    pesi.append(int(p))
                for p,n in enumerate(nodi_vicini):
                    riga[n] = pesi[p]
                matrice.append(riga)
                error=False
            except:
                print("Si è verificato un errore, riprovare")
                error=True

    return matrice

def dijkstra(matrice,node):
    if len(matrice)-1 < node:
        print("Non esiste il nodo inserito")
        return 0;
    percorsi={}
    predecessori={}
    nodi_disponibili=[]
    cont=0
    for i in range(0,len(matrice)):
        nodi_disponibili.append(cont)
        percorsi[str(cont)]=-1
        predecessori[str(cont)]="non presente"
        cont += 1

    nodo = node
    percorsi[str(node)]=0
    predecessori[str(node)]=str(nodo)
    end=True
    while len(nodi_disponibili)!=0 and end:
        for nr,_ in enumerate(matrice):
            if matrice[nodo][nr] > -1:
                if percorsi[str(nr)] > percorsi[str(nodo)]+matrice[nodo][nr] or percorsi[str(nr)]==-1:
                    percorsi[str(nr)]=percorsi[str(nodo)]+matrice[nodo][nr]
                    predecessori[str(nr)]=str(nodo)
        nodi_disponibili.remove(nodo)
        nodo_p=nodo
        min=9999
        for i in nodi_disponibili:
            if percorsi[str(i)] > -1:
                if percorsi[str(i)] < min:
                    nodo = i
                    min = percorsi[str(i)]
        if nodo == nodo_p:
            end=False
    return percorsi, predecessori

def main():
    scacchiera = []
    scacchiera = MatricePesataOrientata()
    nodo = -1
    while nodo == -1:
        nodo = int(input("inserire il nodo a cui applicare dijkstra:  "))
        if len(scacchiera)-1 < nodo:
            print("Non esiste il nodo inserito")
            nodo=-1
    percorsi = {}
    predecessori = {}
    percorsi, predecessori = dijkstra(scacchiera,nodo)
    print(percorsi)
    print(predecessori)
    
if __name__ == "__main__":
    main()
