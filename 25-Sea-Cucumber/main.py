import os
import time

def parseInput(filename):
    with open(filename+'.txt', 'r') as file:
        lines = file.read().split('\n')
    seeFloor = []
    for line in lines:
        seeFloor.append(list(line))
    return seeFloor

def pprint(seeFloor, step = 0):
    os.system('clear')
    map = {'.': ' ', 'v': '↓', '>':'→'}
    print('\n┌'+'─'*(len(seeFloor[0])+2) +'┐')
    for i in seeFloor:
        print('│ ',end='')
        for j in i:
            print(map[j], end='')
        print(' │')
    print('└'+'─'*(len(seeFloor[0])+2) +'┘')
    print('[STEP '+'% 3d' % step+']')
    time.sleep(.1)
# ==================================================

def advance(seeFloor):
    nextSeeFloor = [['.' for i in range(len(seeFloor[0]))] for j in range(len(seeFloor))]
    moving = False
    # going right
    for i in range(len(seeFloor)):
        for j in range(len(seeFloor[0])):
            if seeFloor[i][j] == '>' \
                and seeFloor[i][(j+1)%len(seeFloor[i])] == '.':
                nextSeeFloor[i][j] = '.'
                nextSeeFloor[i][(j+1)%len(seeFloor[i])] = '>'
                moving = True
            elif seeFloor[i][j] == '>':
                nextSeeFloor[i][j] = '>'

    # then going down
    for i in range(len(seeFloor)):
        for j in range(len(seeFloor[0])):
            # has a moving one, the next place has not already a down, and not already taken y a going-right-one
            if seeFloor[i][j] == 'v' \
                and seeFloor[(i+1)%len(seeFloor)][j] != 'v' \
                and nextSeeFloor[(i+1)%len(seeFloor)][j] == '.':
                nextSeeFloor[i][j] = '.'
                nextSeeFloor[(i+1)%len(seeFloor)][j] = 'v'
                moving = True
            elif seeFloor[i][j] == 'v':
                nextSeeFloor[i][j] = 'v'

    return nextSeeFloor, moving

# ==================================================

seeFloor = parseInput('input')
pprint(seeFloor)
step = 0
moving = True
while moving:
    step += 1
    seeFloor, moving = advance(seeFloor)
    pprint(seeFloor, step)

print('Moving:',moving)
print('Steps:',step)