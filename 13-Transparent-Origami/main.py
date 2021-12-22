def parseInput(filename):
    with open(filename+'.txt', 'r') as file:
        lines = file.read().split('\n\n')

    coordinates = list(map(lambda line: [
        int(line.split(',')[0]),
        int(line.split(',')[1])
    ], lines[0].split('\n')))

    instructions = []
    for i in lines[1].split('\n'):
        i = i.replace('fold along ', '')
        ax, nb = i.split('=')
        instructions += [[ax, int(nb)]]

    return coordinates, instructions

def prettyPrint(matrix):
    map = {0: '  ', 1:'██'}
    for i in matrix:
        for j in i:
            if j not in map: j=1
            print(map[j], end='')
        print('')
    print('---')

def createMatrix(coord):
    allXs = list(map(lambda c: c[1], coord))
    allYs = list(map(lambda c: c[0], coord))
    maxX = max(allXs)+1
    maxY = max(allYs)+1
    matrix = [[0 for i in range(maxY)] for j in range(maxX)]
    for c in coord:
        matrix[c[1]][c[0]] = 1
    return matrix

def foldMatrixVertically(matrix, foldPos):
    # wow, just realised i just folded in half and it kept working

    left = [ [matrix[i][j] for j in range(len(matrix[0])//2)] \
        for i in range(len(matrix)) ]
    right = [ [matrix[i][j] for j in range(len(matrix[0])//2+1, len(matrix[0]))] \
        for i in range(len(matrix)) ]

    for i in range(len(right)):
        posLeft = len(left[0]) - 1
        for j in range(len(right[0])):
            # print(i,j, '->',i,posLeft)
            if right[i][j] > 0: left[i][posLeft] += 1
            posLeft -= 1
    return left

def foldMatrixHorizontally(matrix, foldPos):
    top = matrix[:foldPos]
    bottom = matrix[foldPos+1:]

    posTop = len(top) - 1
    for i in range(len(bottom)):
        for j in range(len(bottom[0])):
            if bottom[i][j] > 0: top[posTop][j] += 1
        posTop = posTop - 1
    return top

'''Part 1 : count number of dots after first folding'''
def countScored(matrix):
    count = 0
    for i in matrix:
        for j in i:
            if j > 0:
                count += 1
    return count

# =========================================================

coordinates, instructions = parseInput('input')
matrix = createMatrix(coordinates)
for i in instructions:
    if i[0] == 'y': matrix = foldMatrixHorizontally(matrix, i[1])
    else: matrix = foldMatrixVertically(matrix, i[1])
prettyPrint(matrix)