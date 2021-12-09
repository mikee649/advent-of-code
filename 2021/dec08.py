input_file = open('input08.txt', 'r')
lines = input_file.readlines()

signatureToPosition = {
    '[3, 5, 5, 5, 6, 6, 6, 7]': 't',
    '[4, 5, 5, 5, 6, 6, 7]': 'm',
    '[5, 5, 5, 6, 6, 6, 7]': 'b',
    '[4, 5, 6, 6, 6, 7]': 'tl',
    '[2, 3, 4, 5, 5, 6, 6, 7]': 'tr',
    '[5, 6, 6, 7]': 'bl',
    '[2, 3, 4, 5, 5, 6, 6, 6, 7]': 'br'
}

positionsToValue = {
    't,tl,tr,bl,br,b': 0,
    'tr,br': 1,
    't,tr,m,bl,b': 2,
    't,tr,m,br,b': 3,
    'tl,tr,m,br': 4,
    't,tl,m,br,b': 5,
    't,tl,m,bl,br,b': 6,
    't,tr,br': 7,
    't,tr,tl,m,bl,br,b': 8,
    't,tl,tr,m,br,b': 9
}

def get_letter_positions(seq):
    positionToLetter = {}
    
    for char in ['a','b','c','d','e','f','g']:
        signature = []
        for string in seq.split(' '):
            if char in string:
                signature.append(len(string))
        signature.sort()

        positionToLetter[signatureToPosition[str(signature)]] = char
    
    return positionToLetter

def get_string_values(positionToLetter):
    stringToValue = {}

    for positions, value in positionsToValue.items():
        positions = positions.split(',')
        string = ''
        for pos in positions:
            string += positionToLetter[pos]
        stringToValue[str(sorted(string))] = value

    return stringToValue
        

count = 0
outputSum = 0

for line in lines:
    positionToLetter = get_letter_positions(line.split(" | ")[0])
    stringToValue = get_string_values(positionToLetter)

    output = line.split(" | ")[1]
    decodedOutput = 0

    for string in output.split(" "):
        if len(string.rstrip()) in [2,3,4,7]:
            count += 1

        decodedOutput *= 10
        decodedOutput += stringToValue[str(sorted(string.rstrip()))]
    
    outputSum += decodedOutput

print('--- Part One ---')
print(count)
print('--- Part Two ---')
print(outputSum)
