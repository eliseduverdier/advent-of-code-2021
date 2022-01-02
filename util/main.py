def getInput(name):
    with open(name+'.txt', 'r') as file:
        return file.read().strip().split('\n')

def part1():
    return

def part2():
    return


input = getInput('sample')
# input = getInput('input')

print('part 1:', part1())
print('part 2:', part2())