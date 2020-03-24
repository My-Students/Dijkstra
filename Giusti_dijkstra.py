#nome: Matteo Giusti

def pavimento():
    pavimento = open("data.txt","r")
    linea = pavimento.readlines()
    mat = []
    dim  = 0
    for i in linea:
        vet = []
        celle = i.replace("\n","").split(" ")
        for k in celle:
            if celle == "True":
                vet.append(True)
            elif celle == "False":
                vet.append(False)
                dim = dim + 1
        mat.append(vet)
    
    return mat,dim

def creaPavimento(pavimento):
    mat1 = []
    cont  = 0
    for i in range(0,len(pavimento)):
        vet1 = []
        for k in range(0,len(pavimento)):
            if pavimento[i][k] == True:
                vet1.append(cont)
                cont = cont + 1
            else:
                vet1.append(-1)
        mat1.append(vet1)
    return mat1

def creaMatrice(mat,dim):
    matAd = []
    for i in range(0,dim):
        vet = []
        for k in range(0,dim):
            vet.append(0)
        matAd.append(vet)

    for i in range(0,len(mat)):
        for k in range(0,len(mat)):
            if mat[i][k] != -1:
                va  = mat[i][k]
                if i + 1 < len(mat):
                    if mat[i+1][k] != -1:
                        va2 = mat[i+1][k]
                        matAd[va][va2] = 1
                        matAd[va2][va] = 1
                if k + 1 < len(mat):
                    if mat[i][k+1] != -1:
                        va2 = mat[i][k+1]
                        matAd[va][va2] = 1
                        matAd[va2][va] = 1        
    return matAd        

def stampa(matAd):
    for i in range(0, len(matAd)):
        print("\t")
        for k in range(0,len(matAd)):
            print(matAd[i][k])

def dijkstra(matAd, source):
    vet=[]
    dist = []
    for i in range(source, len(matAd)):
        dist[i] = 10000000
    dist[source] = 0
    successivo = []
    
    for i in range(0,len(matAd)):
        successivo.append(i)

    while len(successivo)!= 0:
        Min = min(dist)
        nodo = successivo.pop(dist.index(Min))
        dist.remove(Min)
        vet.append(nodo)

        for vicini in matAd[nodo]:
            if vicini > 0 and matAd[nodo].index(vicini) in successivo:
                if vicini + Min < dist[successivo.index((matAd[nodo].index(vicini)))]:

                    dist[successivo.index((matAd[nodo].index(vicini)))] = vicini + Min
            matAd[nodo][matAd[nodo].index(vicini)] = 0
    print(vet)
        

def main():
  mat,dim = pavimento()
  matAd = creaMatrice(mat,dim)
  stampa(matAd)
  source = int(input("inserisci il nodo di partenza: "))
  dijkstra(matAd,source)


if __name__ == '__main__':
    main()