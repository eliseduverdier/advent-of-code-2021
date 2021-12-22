with open('input.txt', 'r') as file:
    numbers = file.read().split(',')
numbers = list(map(lambda nb: int(nb), numbers))

''' bruteforce (:'''
def part1(numbers, until):
    generation = 0
    while generation < until:
        for i in range(len(numbers)):
            if (numbers[i] == 0):
                numbers[i] = 7
                numbers += [8]
            numbers[i] -= 1
        generation += 1
    return len(numbers)

def part2(numbers, until):
    # count 0 1 2 3 4 5 6 7 8 s
    ages = [0,0,0,0,0,0,0,0,0]
    # count firsts fishes
    for i in numbers: ages[i] += 1

    # let's grow
    generation = 0
    while generation < until:
        zeroes = ages.pop(0)
        ages[6] += zeroes # zeroes restart at 6,
        ages += [zeroes] # ...spawning new 8 babies
        generation += 1
    return sum(ages)

# print(part1(numbers, 80))
# print(part2([1,2,3,3,4], 256))
print(part1(numbers, 80))
print(part2(numbers, 256))