''' Parse input file, returning list of ints + matrices of boards'''
def parseInput(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n\n')
    numbersList, boardsList = lines[0], lines[1:]
    numbers = list(map(lambda i: int(i), numbersList.split(',')))
    boards = []
    for b in boardsList:
        board = []
        for line in b.split('\n'):
            nbs = []
            for i in line.split(' '):
                if i != '': nbs += [int(i)]
            board += [nbs]
        boards += [board]

    return numbers, boards

def removeFoundNumbers(boards, targetNumber):
    # print('TARGET ', targetNumber) #,' //// ',boards
    for i in range(len(boards) ):
        for j in range(len(boards[i])):
            for k in range(len(boards[i][j])):
                if boards[i][j][k] == targetNumber:
                    boards[i][j][k] = -1
    return boards

'''return bool + board index '''
def hasBingo(boards):
    verticalBingo, idxV = hasVerticalBingo(boards)
    horizontalBingo, idxH = hasHorizontalBingo(boards)
    if (verticalBingo): return verticalBingo, idxV
    if (horizontalBingo): return horizontalBingo, idxH
    else: return False, 0

def hasHorizontalBingo(boards):
    for i in range(len(boards) ):
        for j in range(len(boards[i])):
            if sum(boards[i][j]) == -5:
                return True, i
    return False, -1

def hasVerticalBingo(boards):
    for i in range(len(boards)):
        # get sum of each column
        for k in range(len(boards[i][0])):
            col = []
            for j in range(len(boards[i])):
                col += [ boards[i][j][k] ]
            if sum(col) == -5:
                return True, i
    return False, -1

def sumRemaining(board):
    remaining = []
    for i in range(len(board)):
        remaining += list(filter(lambda x: x != -1, board[i]))
    print ('remaining: ', remaining)
    return sum(remaining)

# =================================================

def part1(numbers, boards):
    for number in numbers:
        removeFoundNumbers(boards, number)
        bingo, winningBoard = hasBingo(boards)
        if bingo:
            print('BINGO !!! for #',boards[winningBoard],' with ',number)
            sum = sumRemaining(boards[winningBoard])
            return sum, number

def part2(numbers, boards):
    for number in numbers:
        removeFoundNumbers(boards, number)
        if len(boards) > 1:
            bingo, index = hasBingo(boards)
            while bingo:
                bingo, index = hasBingo(boards)
                if (bingo): del boards[index]
        else:
            bingo, index = hasBingo(boards)
            if bingo:
                return sumRemaining(boards[0]), number

print('================================== day 04 ===============')

[numbers, boards] = parseInput('./input.txt')

sum, number = part1(numbers, boards)
print('#1: ',sum,' * ', number,' = ',sum * number)

sum, number = part2(numbers, boards)
print('#2: ',sum,' * ', number,' = ', sum * number)