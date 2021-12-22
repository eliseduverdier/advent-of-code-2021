import numpy as np

def parseInput(filename):
    with open(filename+'.txt', 'r') as file:
        lines = file.read().split('\n')
    matrix = []
    for line in lines:
        matrix += [ list(map(lambda nb: int(nb), list(line))) ]
    return matrix

def prettyPrint(matrix):
    for i in matrix:
        for j in i:
            print(j, end='')
        print('')
    print('---')

# ============================

matrix = np.array(parseInput('sample'))

# part 2, bigger matrix
baseMatrix = np.where(matrix < 9, matrix+1, 1)
for i in range(4):
    matrix = np.hstack((matrix, baseMatrix))
    baseMatrix = np.where(baseMatrix < 9, baseMatrix+1, 1)

baseMatrix = np.where(matrix < 9, matrix+1, 1)
for i in range(4):
    matrix = np.vstack((matrix, baseMatrix))
    baseMatrix = np.where(baseMatrix < 9, baseMatrix+1, 1)
prettyPrint(matrix)

# ============================

maxWeight = 100000
lenX, lenY = matrix.shape
print(lenX, lenY)
lastIndex = lenX*lenY
matrix = matrix.flatten()

visited = np.zeros_like(matrix)
weights = np.full_like(matrix, maxWeight)
visitWeight = np.full_like(matrix, maxWeight)
weights[0] = 0

index = 0
while index < lastIndex:
    if index % lenX == 0: # left of matrix
        neighbours = [index+lenX, index-lenX, index+1]
    elif index % (lenX-1) == 0: # right of matrix
        neighbours = [index+lenX, index-lenX, index-1]
    else: # middle
        neighbours = [index+lenX, index-lenX, index+1, index-1]

    for n in neighbours:
        if n > 0 and n < lastIndex:
            if visited[n] == 0:
                newWeight = weights[index] + matrix[n]
                if newWeight < weights[n]:
                    weights[n] = newWeight
                    visitWeight[n] = newWeight

    visited[index] = 1
    visitWeight[index] = maxWeight
    index += 1

print('final:', weights)
