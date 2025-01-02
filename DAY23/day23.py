data = open('input.txt', 'r').read().split('\n')

def getComputerNetwork():
    network = {}
    for elem in data:
        comp1, comp2 = elem.split("-")
        if comp1 not in network:
            network[comp1] = {comp2}
        else:
            network[comp1].add(comp2)

        if comp2 not in network:
            network[comp2] = {comp1}
        else:
            network[comp2].add(comp1)
    return network

def getTriplets(network):
    values = list(network.values())
    keys = list(network.keys())
    result = set()
    for i in range(len(values)):
        for j in range(i, len(values)):
            if keys[j] in values[i]:
                intersect = values[i].intersection(values[j])
                for elem in intersect:
                    if elem != keys[i] != keys[j]:
                        # result.add(tuple(sorted((elem, keys[i], keys[j]))))
                        result.add((elem, keys[i], keys[j]))
    return result

def getValidTripletsCount(triplets):
    count = 0
    for a,b,c in triplets:
        if 't' == a[0] or 't' == b[0] or 't' == c[0]:
            count += 1

    # return count
    return count//3

network = getComputerNetwork()
triplets = getTriplets(network)
print(getValidTripletsCount(triplets))





