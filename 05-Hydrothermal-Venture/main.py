''' Parse input file, returning list of ints + matrices of boards'''
def parseInput(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n')
    lines = list(map(lambda line: line.replace(' -> ', ',').split(','), lines))
    lineList = []
    for line in lines:
        lineList += [Line(
            Coordinate(int(line[0]), int(line[1])),
            Coordinate(int(line[2]), int(line[3]))
        )]
    return lineList
#====================================================================
class Coordinate:
    def __init__(self, x, y):
         self.x = x
         self.y = y
#--------------------------------------------------------------------
class Line:
    def __init__(self, a, b):
         self.a = a
         self.b = b
    def __repr__(self):
        # return ('({},{})->({},{})',self.a.x,self.a.y,self.b.x,self.b.y)
        return '('+str(self.a.x)+','+str(self.a.y)+')'\
                + '->'\
                +'('+str(self.b.x)+','+str(self.b.y)+')'
    def isOrthogonal(self):
        return self.a.x == self.b.x or self.a.y == self.b.y
#====================================================================
def traceLinesOnPlan(lines):
    max = getPlanSize(lines)
    plan = [ [0]*(max[0]+1) for i in range(max[1]+1)]

    for i in lines:
        # if i.isOrthogonal:  # for part 1
        if i.b.x - i.a.x > 0: Xmove = 1
        elif i.b.x - i.a.x < 0: Xmove = -1
        else: Xmove = 0

        if i.b.y - i.a.y > 0: Ymove = 1
        elif i.b.y - i.a.y < 0: Ymove = -1
        else: Ymove = 0

        drawing = True
        while drawing:
            try:
                plan[i.a.y][i.a.x] += 1
            except Exception as e:
                print('Failed marking point ',str(i))
            if i.a.x == i.b.x and i.a.y == i.b.y:
                drawing = False
            i.a.x += Xmove
            i.a.y += Ymove

    return plan

def getPlanSize(coords):
    maxX, maxY = 0, 0
    for line in coords:
        if line.a.x > maxX: maxX = line.a.x
        if line.b.x > maxX: maxX = line.b.x
        if line.a.y > maxY: maxY = line.a.y
        if line.b.y > maxY: maxY = line.b.y
    return maxX, maxY
def getOverlapped(plan):
    twos = 0
    for i in plan:
        for j in i:
            if j > 1: twos += 1
    return twos


#====================================================================
def printPlan(plan):
    for i in plan:
        for j in i:
            if j == 0: print(' ', end='')
            elif j == 1: print('▒', end='')
            else: print('█', end='')
        print('')
#====================================================================
coordinates = parseInput('input.txt')
plan = traceLinesOnPlan(coordinates)
result = getOverlapped(plan)
printPlan(plan) # pretty !
print('RESULT: ',result)
