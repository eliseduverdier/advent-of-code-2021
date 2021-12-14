def parseInput(filename):
    with open(filename+'.txt', 'r') as file:
        lines = file.read().split('\n\n')

    template = lines[0]
    rulesAr = list(map(lambda i: i.split(' -> '), lines[1].split('\n')))
    rules = {}
    for r in rulesAr:
        rules[r[0]] = r[1]

    return template, rules

'''
Get dictionary for each pair with its number of occurences
'''
def getPairsList(template, rules):
    pairsList = {}
    for p, value in rules.items():
        pairsList[p] = 0

    for i in range(len(template) - 1):
        pairsList[template[i:i+2]] += 1
    return pairsList

'''
Count new pairs, and remove old one
'''
def countPairs(rules, pairsList, letterCount):
    oldPairsList = pairsList.copy()

    for (a, b), new in rules.items():
        count = oldPairsList[a+b]
        pairsList[a+b] -= count
        pairsList[a+new] += count
        pairsList[new+b] += count
        letterCount[new] += count

    return pairsList, letterCount

# =========================================================

template, rules = parseInput('input')
pairsList = getPairsList(template, rules)

letterCount = {}
#init
for p, value in rules.items():
    letterCount[p[0]] = 0
    letterCount[p[1]] = 0
# add from first template
for l in template:
    if l in letterCount: letterCount[l] += 1
    else: letterCount[l] = 1

for i in range(40):
    pairsList, letterCount = countPairs(rules, pairsList, letterCount)

# print(pairsList)
count = list(letterCount.values())
print(max(count) - min(count))


