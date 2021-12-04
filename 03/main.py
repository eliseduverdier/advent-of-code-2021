def parseInput(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n')
    matrix = []
    for line in lines:
        matrix += [list(line)]
    return matrix
# =========================
def getCols(matrix):
    if matrix == []: return []
    lines = []
    for i in range(len(matrix[0])):
        lines += [ ''.join(getNthCol(matrix, i)) ]
    return lines

'''if the sum is greater that the mean, then it has more ones'''
def get_most_common(array):
    intarray = list(map(lambda i: int(i), array))
    if sum(intarray) >= len(intarray)/2:
        return '1'
    else:
        return '0'

'''diff implem: count them'''
def get_least_common(array, i):
	ones, zeros = 0, 0
	for nb in array:
		ones += 1 if nb[i] == '1' else 0
		zeros += 1 if nb[i] == '0' else 0
	return '1' if ones < zeros else '0'

def getNthCol(matrix, col):
    l = []
    for i in range(len(matrix)):
        l += matrix[i][col]
    return l

# ========================
def getGammas(array):
    binaryNb = ''
    for i in array:
        binaryNb += get_most_common(i)
    return binaryNb

'''epsilons are just inverted gammas :)'''
def invert(string):
    inverted = ''
    for l in string:
        if l == '0': inverted += '1'
        else: inverted += '0'
    return inverted
# ========================
'''
recursively get the numbers starting with the most common number
building the output number at each step
'''
def getOxygenRating(matrix, keeping):
    if matrix == [[]]:
        return keeping
    keep = [] # numbers staring with most common nb
    most_common = get_most_common(getCols(matrix)[0])
    for i in matrix:
        keep = []
        if i[0] == most_common:
            keep += [i[1:]]
    return getOxygenRating(keep, keeping + most_common)

'''
looping through numbers, filtering only the least_commons ones
'''
def getCO2Rating(matrix):
	matrixcp = matrix[::1]
	i = 0
	max_i = len(matrixcp)
	while len(matrixcp) > 1 and i <= max_i:
		least_common = get_least_common(matrixcp, i)
		matrixcp = list(filter(lambda x: x[i] == least_common, matrixcp))
		i += 1
	return matrixcp[0]

# ========================

matrix = parseInput('input.txt')
# PART 1
#gammas = getGammas(getCols(matrix))
#epsilons = invert(gammas)
#print(int(gammas, 2) * int(epsilons, 2))

# PART 2
oxygenGenRating = getOxygenRating(matrix, '')
CO2Rating = ''.join(getCO2Rating(matrix))

print(int(oxygenGenRating, 2) * int(CO2Rating, 2))

