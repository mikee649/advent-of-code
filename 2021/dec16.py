import functools

input_file = open('input16.txt', 'r')
hexData = input_file.readlines()[0].rstrip()

binData = bin(int(hexData, 16))[2:]
if len(binData) % 4 != 0:
    binData = "0" * (4 - len(binData) % 4) + binData

typeMap = {
    0: 'sum',
    1: 'product',
    2: 'min',
    3: 'max',
    4: 'literal',
    5: 'greater than',
    6: 'less than',
    7: 'equal to'
}

versionSum = 0


def parseLiteralValue(index):
    binValue = ''

    while True:
        terminator = binData[index]
        index += 1
        binValue += binData[index:index + 4]
        index += 4
        if terminator == '0':
            break

    return [int(binValue, 2), index]


def parse(index):
    global versionSum

    version = int(binData[index:index + 3], 2)
    versionSum += version
    index += 3
    typeID = int(binData[index:index + 3], 2)
    index += 3

    if typeMap[typeID] == 'literal':
        value, index = parseLiteralValue(index)
        return [{'typeID': typeID, 'subPackets': [value]}, index]
    else:
        lengthTypeID = binData[index]
        index += 1
        subPackets = []

        if lengthTypeID == '0':
            length = int(binData[index:index + 15], 2)
            index += 15
            terminateIndex = index + length
            while index < terminateIndex:
                value, index = parse(index)
                subPackets.append(value)
        else:
            numPackets = int(binData[index:index + 11], 2)
            index += 11
            for i in range(numPackets):
                value, index = parse(index)
                subPackets.append(value)

        return [{'typeID': typeID, 'subPackets': subPackets}, index]


def compute(packet):
    if typeMap[packet['typeID']] == 'literal':
        return packet['subPackets'][0]

    computedSubPackets = list(map(lambda p: compute(p), packet['subPackets']))

    if typeMap[packet['typeID']] == 'sum':
        return sum(computedSubPackets)
    elif typeMap[packet['typeID']] == 'product':
        return functools.reduce(lambda x, y: x * y, computedSubPackets)
    elif typeMap[packet['typeID']] == 'min':
        return min(computedSubPackets)
    elif typeMap[packet['typeID']] == 'max':
        return max(computedSubPackets)
    elif typeMap[packet['typeID']] == 'greater than':
        return 1 if computedSubPackets[0] > computedSubPackets[1] else 0
    elif typeMap[packet['typeID']] == 'less than':
        return 1 if computedSubPackets[0] < computedSubPackets[1] else 0
    elif typeMap[packet['typeID']] == 'equal to':
        return 1 if computedSubPackets[0] == computedSubPackets[1] else 0


parsedPacket = parse(0)

print('--- Part One ---')
print(versionSum)
print('--- Part Two ---')
print(compute(parsedPacket[0]))
