# https://realpython.com/how-to-implement-python-stack/

def parseInput(filename):
    with open(filename+'.txt', 'r') as file:
        lines = file.read().split('\n')
    return list(map(lambda line: list(line), lines))

points1 = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137,
}
points2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}
closingMatch = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}
openMatch = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
closingList = [')', ']', '}', '>']

# =========================================================

def isCorrupted(line):
    testLine = parse(line, 0)
    if not testLine[0]:
        return testLine[1] # the culprit
    else: return None

def hasOnlyOpen(stack):
    for c in stack:
        if c in closingList:
            return False
    return True

def parse(stack, i):
    if len(stack) == 0 or hasOnlyOpen(stack):
        return True, stack
    if stack[i] in closingList:
        if closingMatch[stack[i]] == stack[i-1]:
            stack.pop(i)
            stack.pop(i-1)
            return parse(stack, i-1)
        else: # match error!
            return False, stack[i]
    return parse(stack, i+1)

def closeLine(openings):
    ends = []
    while len(openings) > 0:
        ends.append( openMatch[openings.pop()] )
    return ends

# =========================================================

lines = parseInput('input')

score = 0
endScores = []
for l in lines:
    endCurrentScore = 0
    culprit = isCorrupted(l)
    if culprit != None:
        # PART 1:
        # score += points1[culprit]
        del(l)
    else:
        # PART 2
        end = closeLine(l)
        for e in end:
            endCurrentScore = endCurrentScore * 5 + points2[e]
        endScores += [endCurrentScore]
endScores.sort()
print('>>>', endScores[len(endScores) // 2])