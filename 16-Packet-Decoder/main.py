from functools import reduce

def parseInput(filename):
    with open(filename+'.txt', 'r') as file:
        return file.read()

d = { '0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011', '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111', '8' : '1000', '9' : '1001', 'A' : '1010', 'B' : '1011', 'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111', }
# ==============================================================
def decode(hexa):
    bin = [d[char] for char in hexa]
    return ''.join(bin)

sumVersions = 0
def parse(packets):
    global sumVersions
    version = int(packets[:3], 2)
    type = int(packets[3:6], 2)
    sumVersions += version
    # print(f'v {version}') # / type {packetTypeId}')
    start = 6
    bits = []

    if type == 4: # packet is a literal value
        for i in range(6, len(packets), 5):
            start += 5
            bits.append(packets[i+1: i+5])
            if packets[i] == '0':
                break
        bits = int(''.join(bits), 2)

    else: # packet is an operator
        start += 1
        if packets[6] == '1':
            typeLen = 11
            subPacketCount = int(packets[start: start+typeLen], 2)
            start += typeLen
            subPacket = packets[start:]
            for i in range(subPacketCount):
                res = parse(subPacket)
                bits.append(res)
                start += res[0]
                subPacket = packets[start:]
        elif packets[6] == '0': # typeLen == 15:
            typeLen = 15
            subPacketLen = int(packets[start: start+typeLen], 2)
            subPacket = packets[start+typeLen:]
            start += typeLen + subPacketLen
            i = 0
            while i < subPacketLen:
                res = parse(subPacket[i:])
                bits.append(res)
                i += res[0]

    return start, type, bits

def computeResult(data):
    op = data[1]
    if op == 4: return data[2]

    bits = []
    for sub in data[2]:
        bits.append(computeResult(sub))

    if op == 0: return sum(bits)
    elif op == 1: return reduce((lambda x, y: x * y), bits)
    elif op == 2: return min(bits)
    elif op == 3: return max(bits)
    elif op == 5: return 1 if bits[0] > bits[1] else 0
    elif op == 6: return 1 if bits[0] < bits[1] else 0
    elif op == 7: return 1 if bits[0] == bits[1] else 0


input = parseInput('input')
# input = '880086C3E88112'
# input = '9C0141080250320F1802104A08'
data = parse(decode(input))
# print ( data )
print ( sumVersions )
res = computeResult(data)
print ( res )