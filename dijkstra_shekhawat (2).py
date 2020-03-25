grafo = {'a':{'b':1,'c':4},'b':{'c':1, 'd':3},'c':{'d':1},'d':{}}  #dizionario del grafo con una slite modifica
#grafo_prova = {0:{1:1, 2:4}, 1:{2:1 , 3:3}, 2:{3:1}, 3:{}}

def dijkstra(grafo,start):
    shot_path = {} # Contiene il numero minimo di costo per raggiungere un certo nodo 
    grafoNodes = grafo #Conterrà il grafo per poi sapere quante volte esegure una certa cosa
    infinity = 100000 #Un numero abbastanza grande da non essere superato


    for node in grafoNodes: #Inizializzo tutti i nodi a infinito tranne il primo
        shot_path[node] = infinity
    shot_path[start] = 0 

    while grafoNodes:               # Eseguiro  fino a quando non sarà esaurito il grafo
        minNode = None              # il nodo minino alla creazione non esiste, quindi None
        for node in grafoNodes:     # Cerco il nodo minimo per settarmi sù di esso e cercare poi i prossimi etc..
            if minNode is None:
                minNode = node
            elif shot_path[node] < shot_path[minNode]:
                minNode = node

        for childNode, weight in grafo[minNode].items():                # Faccio un ciclo per ogni elmento di ogni blocco della dello shot_path
            if weight + shot_path[minNode] < shot_path[childNode]:      # controllo per vedere se il peso + l'etichetta nel mio nodo sono minori di quelli sucessivi(figli) 
                shot_path[childNode] = weight + shot_path[minNode]      # se vero, rietichetto il nodo figlio con un valore minore
        grafoNodes.pop(minNode)    # mi permette di uscire dal while
    
   
    print(shot_path)


if __name__ == "__main__":
    dijkstra(grafo, 'a')