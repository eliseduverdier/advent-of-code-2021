from collections import Counter

def getInput(name):
    with open(name+'.txt', 'r') as file:
        return list(map(
            lambda i: i.split('-'), file.read().split('\n')
        ))

def prettyPrint(dictionary):
    for d in dictionary:
        print('-',d,':', dictionary[d])

# ============================================================

'''
Set the graph as {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
'''
def graphFromTunnels(tunnels):
    graph = {
        'start': [],
    }
    # init start, end, an other keys
    for t in tunnels:
        if t[0] == 'start': graph['start'] += [t[1]]
        if t[1] == 'start': graph['start'] += [t[0]]
        if t[1] == 'end': graph[t[0]] = ['end']
        if t[0] == 'end': graph[t[1]] = ['end']
        if t[0] not in graph: graph[t[0]] = []
        if t[1] not in graph: graph[t[1]] = []
    for t in tunnels:
        if 'start' not in t and 'end' not in t:
            graph[t[0]] += [t[1]]
            graph[t[1]] += [t[0]]
    del(graph['end'])
    return graph

def isSmallCave(node):
    return node.lower() == node and node != 'end' and node != 'start'

'''
all paths you find should visit small caves at most once,
and can visit big caves any number of times.
'''
def part1(graph, path=['start']):
    count = 0
    for cave in graph[path[-1]]:
        if not (isSmallCave(cave) and cave in path):
            if cave == 'end': count +=1
            else: count += part1(graph, path + [cave])
    return count

'''
big caves can be visited any number of times, (ok)
a single small cave can be visited at most twice, (ok)
and the remaining small caves can be visited at most once. (ok)
'''
def part2(graph, path=['start']):
    count = 0
    for cave in graph[path[-1]]:
        if cave == 'end':
            count += 1
            continue
        smallCaveVisited = [cave for cave in path if isSmallCave(cave)]
        smallCaveVisitedCount = Counter(smallCaveVisited)

        # if its a big cave,
        # or it hasnt been visited before
        # or it has visited before, but only once
        #    AND no other have been visited before twice
        if not isSmallCave(cave) \
            or not cave in path\
            or (smallCaveVisitedCount[cave] == 1 \
                and not 2 in dict(smallCaveVisitedCount).values()):
            count += part2(graph, path + [cave])
    return count

tunnels = getInput('input')
graph = graphFromTunnels(tunnels)
prettyPrint(graph)

print('COUNT 1:',part1( graph ))
print('COUNT 2:',part2( graph ))