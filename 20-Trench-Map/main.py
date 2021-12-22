import time
import os
import copy


def parseInput(filename):
    with open(filename+'.txt', 'r') as file:
        lines = file.read().split('\n\n')

    matrix = []
    for line in lines[1].split('\n'):
        matrix.append( list(map(lambda char: 1 if char == '#' else 0, list(line))) )
    return lines[0], matrix

def prettyPrint(matrix, step):
    os.system('clear')
    print(f'[[[[[[[[[[[[[[[[[[[[ STEP {step}]]]]]]]]]]]]]]]]]]]]]]')
    for i in matrix:
        for j in i:
            print('#' if j == 1 else '.', end='')
        print('')
    print('---')
    # time.sleep(.5)

#====================================================================
def ENHANCE(matrix, a, b, algo, oddStep):
    output = ''
    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                output += str(matrix[a + i][b + j])
            except IndexError:
                output += '0' if oddStep else '1'
    # print(output, '->', int(output, 2), '->',  algo [ int(output, 2) ])
    return 1 if algo [ int(output, 2) ] == '#' else 0

def countLitCells(matrix):
    count = 0
    for i in matrix:
        for j in i:
            if j == 1:
                count += 1
    return count

#====================================================================
algo, matrix = parseInput('input')

# background of unlit pixels
size = 100
padMatrix = [[0 for i in range(len(matrix[0]) + size*2)] for j in range(len(matrix) + size*2)]
for a in range(len(matrix)):
    for b in range(len(matrix[0])):
        padMatrix[a+(size)][b+(size)] = matrix[a][b]
matrix = [row[:] for row in padMatrix]

# prettyPrint(matrix)
steps = 50
for step in range(1,steps+1):
    # background of unlit pixels
    # newmatrix = [[0 for i in range(len(matrix[0]) + step*2)] for j in range(len(matrix) + step*2)]
    newmatrix = [row[:] for row in matrix] # deep copy

    for a in range(len(matrix)):
        for b in range(len(matrix[0])):
            newmatrix[a][b] = ENHANCE(matrix, a, b, algo, step%2==1)
    prettyPrint(newmatrix, step)
    matrix = [row[:] for row in newmatrix] # deep copy

print(countLitCells(matrix))
