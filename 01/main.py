def getInput():
    with open('input.txt', 'r') as file:
        data = file.read().split('\n')
        data = list(map(lambda i: int(i), data))
    return data

def part1(data):
    count = 0
    for nb in range(1, len(data)):
        if data[nb] > data[nb-1] :
            count += 1
    return count

def part2(data):
    count = 0
    for nb in range(3, len(data)):
        if sum(data[nb-2:nb]) > sum(data[nb-3:nb-1]):
            count += 1
    return count

data = getInput()
print(part1(data))
print(part2(data))