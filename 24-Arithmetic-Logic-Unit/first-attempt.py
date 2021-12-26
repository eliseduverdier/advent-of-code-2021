# don't read that: keeping for nostalgia, but it takes years to run

def parseInput(filename):
    instructions = []
    with open(filename+'.txt', 'r') as file:
        lines = file.read().split('\n')
    for line in lines:
        line = line.split(' ')
        instructions.append((line[0], line[1] if len(line) == 2 else line[1:]))
    return instructions

def parseTarget(target, vars):
    if target in ['w','x','y','z']:
        target = vars[target]
    else:
        target = int(target)
    return target

# ===============================================

# instructions = parseInput('sample-binary')
instructions = parseInput('input')
memo = {}
def generateModelNb(instructions, inputMonad):
    vars = { 'w': 0, 'x': 0, 'y': 0, 'z': 0, }
    inputIndex = 0
    for i in instructions:

        if i[0] == 'inp':
            vars[ 'w' ] = int( inputMonad[ inputIndex ] )
            inputIndex += 1
            continue
        target = parseTarget(i[1][1], vars)
        # if (vars, op, target) in memo:
        op = i[0]
        if op == 'add':
            vars[ i[1][0] ] += target
        elif op == 'mul':
            vars[ i[1][0] ] *= target
        elif op == 'mod':
            vars[ i[1][0] ] %= target
        elif op == 'div':
            vars[ i[1][0] ] //= target
        elif op == 'eql':
            vars[ i[1][0] ] = 1 if vars[ i[1][0] ] == target else 0
        # memo[(vars, op, target)] = target

    return vars

# mh nope that will take years:
for nb in range (99999999999999, 11111111111111, -1):
    if nb % 100000 == 0: print(nb)
    if '0' in str(nb): continue # The digit 0 cannot appear in a model number.
    resultingVars = generateModelNb(instructions, str(nb))
    # print(nb, resultingVars['z'])
    if resultingVars['z'] == 0:
        print('valid',nb, resultingVars)
