from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

def buildGraph(wordFile):
    dictionary = {}
    graph = Graph()
    wfile = open(wordFile, 'r')

    for line in wfile.read().split():
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in dictionary:
                dictionary[bucket].append(word)
            else:
                dictionary[bucket] = [word]

    for bucket in dictionary.keys():
        for word1 in dictionary[bucket]:
            for word2 in dictionary[bucket]:
                if word1 != word2:
                    graph.addEdge(word1, word2)
    
    return graph


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)

    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()

        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
            
        currentVert.setColor('black')


hello = "hello.txt"
prueba = buildGraph(hello)

start = Vertex(prueba.getVertex(0))
print(bfs(prueba, start))
