import time
import os
import random

def parseInput(filename):
    with open(filename+'.txt', 'r') as file:
        lines = file.read().split('\n')
    matrix = []
    for line in lines:
        matrix += [ list(map(lambda nb: int(nb), list(line))) ]
    return matrix

def generateRandomInput(sizeX, sizeY):
    return [[random.randint(0,9) for i in range(sizeX)] for j in range(sizeY)]

#====================================================================

def printPretty(matrix):
    for i in matrix:
        for j in i:
            print('% 3d' % j, end='')
        print('')
    print('---')

def printWhao(matrix, step):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n\n--- [STEP '+'% 3d' % step+'] ---')
    map = {0:'✨',   1:'  ',   2:'░░', 3:'░░',   4:'▒▒',5:'▒▒',   6:'▓▓',7:'▓▓',   8:'██', 9:'██'}
    for i in matrix:
        for j in i:
            print(map[j], end='')
        print('')

#====================================================================
def increaseNeighbours(matrix, a, b):
    for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if not (i == 0 and j == 0) and matrix[a][b] > 0:
                        matrix[a + i][b + j] += 1
                except IndexError:
                    pass
    return matrix

def hasReadyToFlash(matrix):
    for i in matrix:
        for j in i:
            if j > 9: return True
    return False

def compute(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] += 1

    while hasReadyToFlash(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] > 9:
                    matrix = increaseNeighbours(matrix, i, j)
                    matrix[i][j] = 0
                    count += 1
    return matrix, count

def beholdOctopusMegaLights(matrix):
    for i in matrix:
        for j in i:
            if j != 0: return False
    return True

# =========================================================

# matrix = parseInput('pretty')
matrix = generateRandomInput(100, 60)
count = 0
steps = 0
for i in range(1000):
    time.sleep(.1)
    printWhao(matrix, steps)
    matrix, countStep = compute(matrix)
    count += countStep
    steps += 1
    if beholdOctopusMegaLights(matrix):
        break
print('Count:',count)
print('Steps:',steps)