import numpy as np

def getTriangularNumber(n):
    return int(n*(n+1)/2)

def getInput(name):
    with open(name+'.txt', 'r') as file:
        numbers = file.read().split(',')
    return list(map(lambda nb: int(nb), numbers))

def getDestinationPart1(positions):
    return int(round(np.median(positions)))

def getDestinationPart2(positions):
    return int(round(np.mean(positions)))

def getFuelCostPart1(positions, destination):
    fuelCost = 0
    for pos in positions:
        fuelCost += abs(pos - destination)
    return fuelCost

def getFuelCostPart2(positions):
    # can't figure out the correct destination :( it's nor the mean, nor the average, nor the median ?
    # will have to calculate each one...
    destinations = range(len(positions))
    fuelCost = [0 for x in range(len(positions))]
    for pos in positions:
        for dest in destinations:
            difference = abs(pos - dest)
            fuelCost[dest] += getTriangularNumber(difference)
    return min(fuelCost)

# ========================= testing =============
positions = getInput('sample')
destination = getDestinationPart2(positions)
fuelCost = getFuelCostPart2(positions, destination)
print('sample destination: (5) ',destination)
print('sample FUEL COST: (168) ',fuelCost)
print('----------------------')
# ==============================================
positions = getInput('input')
fuelCost = getFuelCostPart2(positions)
print('FUEL COST:   ',fuelCost)
