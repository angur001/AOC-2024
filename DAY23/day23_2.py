import networkx as nx

data = open('input.txt', 'r').read().split('\n')

def getComputerNetwork():
    computerGraph = nx.Graph()
    for elem in data:
        comp1, comp2 = elem.split("-")
        computerGraph.add_edge(comp1, comp2)
    return computerGraph

network = getComputerNetwork()
largest_chain = max(list(nx.find_cliques(network)), key=len)
print(','.join(sorted(largest_chain)))

