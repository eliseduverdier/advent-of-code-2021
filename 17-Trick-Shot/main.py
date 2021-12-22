def isInside(pos, target):
    return pos[0] >= target[0][0] and pos[0] <= target[1][0] \
        and pos[1] <= target[0][1] and pos[1] >= target[1][1]

def isAboveAndBefore(pos, target):
    return pos[0] <= target[1][0] and pos[1] >= target[1][1]

# . . . . . . . # . # . . . . .
# . . . . # . . . . . # . . . .
# . . . . . . . . . . . . . . .
# S . . . . . . . . . # . . . .
# . . . . . . . . . . . . . . .
# . . . . . . . . . .(t[0])TTTT
# . . . . . . . . . . #TTTTTTTT
# . . . . . . . . . . TTTTTTTTT
# . . . . . . . . . . TTTTTTTTT
# . . . . . . . . . . TTTTTT(t[1])
# . . . . . . . . . . # . . . .

def part1():
    count = 0
    # target=[( x ,-y ), ( x , -y )]
    target=[(32,-177), (65, -225)]
    # target=[(20,-10), (30, -15)]

    for i in range(66, 0, -1): # (20, 5, -1) :
        for j in range(2000, -226, -1): # (20, 5, -1) :
            step = 0
            missileCoord = [0, 0]
            relativePosition = [0, 0]
            while isAboveAndBefore(relativePosition, target) and step < 3000:
                if isInside(relativePosition, target):
                    count += 1
                    break
                    # print(f'IS INSIDE WITH {i},{j}', relativePosition)
                if step == 0 or missileCoord[0] > 0:
                    missileCoord[0] = i - step
                missileCoord[1] = j - step
                relativePosition[0] += missileCoord[0]
                relativePosition[1] += missileCoord[1]
                step += 1
    return count
print(part1())