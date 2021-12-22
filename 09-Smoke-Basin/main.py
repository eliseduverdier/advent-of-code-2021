def parseInput(filename):
    with open(filename+'.txt', 'r') as file:
        lines = file.read().split('\n')
    matrix = []
    for line in lines:
        numbers = list(line)
        matrix += [ list(map(lambda nb: int(nb), numbers)) ]
    return matrix

# =========================================================

def getNeighbours(matrix, a, b):
    n = []
    if a < len(matrix) - 1: n += [matrix[a+1][b]]
    if b < len(matrix[0]) - 1: n += [matrix[a][b+1]]
    if a > 0: n += [matrix[a-1][b]]
    if b > 0: n += [matrix[a][b-1]]
    return n

def part1(input):
    bassinsCoords = []
    lowPoints = []
    for a in range(len(input)):
        for b in range(len(input[a])):
            n = getNeighbours(input, a, b)
            if min(n) > input[a][b]:
                lowPoints += [input[a][b]]
                bassinsCoords += [[a, b]]


    return sum(lowPoints) + len(lowPoints), bassinsCoords

# =========================================================

def getNeighboursWithout9(matrix, a, b):
    n = []
    # ugly, should have used a list of 4 coordinates
    if a < len(matrix) - 1 and matrix[a+1][b] != 9: n += [matrix[a+1][b]]
    if b < len(matrix[0]) - 1 and matrix[a][b+1] != 9: n += [matrix[a][b+1]]
    if a > 0 and matrix[a-1][b] != 9: n += [matrix[a-1][b]]
    if b > 0 and matrix[a][b-1] != 9: n += [matrix[a][b-1]]
    return n

def getNeighboursCoordinates(matrix, a, b):
    n = []
    if a < len(matrix) - 1 and matrix[a+1][b] != 9 : n += [ [a+1, b] ]
    if b < len(matrix[0]) - 1 and matrix[a][b+1] != 9 : n += [ [a, b+1] ]
    if a > 0 and matrix[a-1][b] != 9 : n += [ [a-1, b] ]
    if b > 0 and matrix[a][b-1] != 9 : n += [ [a, b-1] ]
    return n

def part2(matrix, lowPointsCoords):
    bassinsSize = []
    for low in lowPointsCoords:
        a, b  = low[0], low[1]
        bassinsSize += [ countSize(matrix, a, b) + 1 ]
    bassinsSize.sort()

    return prod(bassinsSize[-3:])

def prod(list):
    p = 1
    for i in list: p *= i
    return p

def countSize(matrix, a, b):
    if matrix[a][b] == 9:
        return 0
    matrix[a][b] = 9 # prevent counting twice
    ns = getNeighboursCoordinates(matrix, a, b)
    if len(ns) == 0:
        return 0
    size = 0
    for n in ns:
        if matrix[n[0]][n[1]] != 9:
            size += countSize(matrix, n[0], n[1]) + 1
    return size

# =========================================================

input = parseInput('input')
sum, lowPointsCoords = part1(input)
print('PART 1: ', sum)
print('PART 2: ', part2(input, lowPointsCoords))