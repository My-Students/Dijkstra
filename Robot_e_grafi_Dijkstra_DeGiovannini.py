"""
Alessia De Giovannini
4°A ROB 
Robot e grafi con Dijkstra
"""
def toDizionario(matr):
    diz = {}
    for i in range(0, len(matr)):
        vet = []
        for j in range(0, len(matr)):
            vet.append(matr[i][j])
        diz['nodo '+ str(i+1)] = vet
    return diz

def leggiPavi():
    file = open("data.txt", "r")
    lines = file.readlines()
    pavi = []
    dim = 0
    for line in lines:
        cells = line.replace("\n", "").split(" ")
        vet = []
        for cell in cells:
            if cell == "True":
                vet.append(True)
            elif cell == "False" :
                vet.append(False)
                dim = dim + 1
            
        pavi.append(vet)
    return pavi, dim

def creazioneCampo(pavi):
    campo = []
    cont = 0
    
    for i in range(0, len(pavi)):
        vet = []
        for j in range(0, len(pavi)):
            if pavi[i][j] == True:
                vet.append(cont)
                cont = cont + 1
            else: 
                vet.append(-1)
        campo.append(vet)
    return campo

def creazioneMatrAdiacenze(campo, dim):
    #Creare Matrice VUOTA
    m = []
    for i in range(0, dim): 
        vet = []
        for j in range(0, dim):
            vet.append(0)
        m.append(vet)

    #Calcolare matrice adiacenze
    for i in range(0, len(campo)):
        for j in range(0, len(campo)):
            if campo[i][j] != -1:
                i2 = campo[i][j]
                if j+1 < len(campo):
                    if campo[i][j+1] != -1:
                        j2 = campo[i][j+1]
                        m[i2][j2] = 1
                        m[j2][i2] = 1
                if i+1 < len(campo):
                    if campo[i+1][j] != -1: 
                        j2 = campo[i+1][j]
                        m[i2][j2] = 1
                        m[j2][i2] = 1
    return m

def dijkstra(mAdiacenze, start, stop):
    daAnalizzare = [start]  #array nodi da analizzare
    visitati = []   #array nodi gia' visitati
    costiCammino =  []  #costi cammino 
    precedenti = []     #array con i migliori precedenti (prec[i] = miglior "precedente" del nodo i-esimo)

    controlloStart = False
    controlloStop = False
    
    for j in mAdiacenze[start]:
        if(j == 1):
            controlloStart = True

    for j in mAdiacenze[stop]:
        if(j == 1):
            controlloStop = True
    
    if(controlloStart == False or controlloStop == False):
        print("Non e' possibile raggiungere il nodo: " + str(stop) + " partendo dal nodo: " + str(start))
    else:
        for i in range(0,len(mAdiacenze)):
            costiCammino.append("inf")
            precedenti.append(i)

        costiCammino[start] = 0
        precedenti[start] = start

        while(daAnalizzare != []):
            nodo = daAnalizzare[0]
            daAnalizzare.pop(0)
            visitati.append(nodo)

            vicini = []
            for j in range(0, len(mAdiacenze)):
                if (mAdiacenze[nodo][j] == 1):
                    vicini.append(j)
                
            for vicino in vicini:
                costoCalcolato = 0
                if(costiCammino[nodo] != "inf"):
                    costoCalcolato = costiCammino[nodo] + 1
                else:
                    costoCalcolato = 1
                
                if((costiCammino[vicino] == "inf") or (costoCalcolato < costiCammino[vicino]) ):
                    costiCammino[vicino] = costoCalcolato
                    precedenti[vicino] = nodo
                    daAnalizzare.append(vicino)     #aggiungo i vicini come nodi da analizzare se il loro costo è minore di quello precedente
            
        camminoMigliore = []
        camminoMigliore.append(stop)
        trovato = False
        i = stop
        while(trovato == False):
            if(precedenti[i] == start):
                trovato = True
            camminoMigliore.append(precedenti[i])
            i = precedenti[i]

        camminoMigliore.reverse()   
        print(camminoMigliore)


def main():
    pavi, dim = leggiPavi()
    dim = len(pavi) * len(pavi) - dim
    campo = creazioneCampo(pavi)
    mAdiacenze = creazioneMatrAdiacenze(campo, dim)
    start = input("inserisci il nodo di partenza: ")
    stop = input("inserisci il nodo di destinazione: ") 
    dijkstra(mAdiacenze, int(start), int(stop))

if __name__ == "__main__":
    main()