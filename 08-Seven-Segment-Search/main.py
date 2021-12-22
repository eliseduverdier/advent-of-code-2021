def getInput(name):
    with open(name+'.txt', 'r') as file:
        lines = file.read().split('\n')
    output = []
    for line in lines:
        parts = line.split(' | ')
        output += [ [parts[0].split(' '), parts[1].split(' ')]]
    return output

# ===================================================================

'''guess the easy numbers from their lengh'''
def guessUnique(digit):
    if len(digit) == 2:
        return 1
    elif len(digit) == 3:
        return 7
    elif len(digit) == 4:
        return 4
    elif len(digit) == 7:
        return 8
    else:
        return None

'''returns an array of the char representation of the digit, on their index'''
def guessFromLength(line):
    number = [i for i in range(10)]
    for strDigit in line:
        digit = guessUnique(strDigit)
        if (digit != None): number[digit] = ''.join(sorted(strDigit))
    return number

'''return true if each segment of smallOne is in bigOne'''
def overlapped(smallOne, bigOne):
    for i in smallOne:
        if i not in bigOne:
            return False
    return True

'''returns true if only N segment is present in both'''
def exactlyNOverlap(N, a, b):
    overlap = [value for value in list(a) if value in list(b)]
    return True if len(overlap) == N else False

# ===================================================================

def part1(input):
    count = 0
    for line in input:
        for char in line[1]:
            if guessUnique(char) != None:
                count += 1
    return count


def part2(input):
    resultNumbersSum = 0
    for line in input:

        numbers = guessFromLength(line[0]) # [-, s, -, -, s, -, -, s, s, -]
        # sort each digit representation alphabetically... they're not in the same order after the pipe
        # guess numbers from their overlap with the others
        for char in line[0]:
            if len(char) == 6 and exactlyNOverlap(3, numbers[7], char) and not overlapped(numbers[4], char):
                numbers[0] = ''.join(sorted(char))
            if len(char) == 5 and exactlyNOverlap(2, numbers[4], char):
                numbers[2] = ''.join(sorted(char))
            if len(char) == 5 and overlapped(numbers[1], char):
                numbers[3] = ''.join(sorted(char))
            if len(char) == 5 and exactlyNOverlap(2, numbers[7], char) and exactlyNOverlap(3, numbers[4], char):
                numbers[5] = ''.join(sorted(char))
            if len(char) == 6 and exactlyNOverlap(1, numbers[1], char) and exactlyNOverlap(3, numbers[4], char):
                numbers[6] = ''.join(sorted(char))
            if len(char) == 6 and overlapped(numbers[4], char):
                numbers[9] = ''.join(sorted(char))

        # deduce the numbers on the right and sum them
        resultNumber = ''
        for char in line[1]:
            resultNumber += str(numbers.index( ''.join(sorted(char)) ))
        resultNumbersSum += int(resultNumber)
    return resultNumbersSum

## ===================================================================

input = getInput('input')

print('PART 1 ', part1(input))
print('PART 2', part2(input))