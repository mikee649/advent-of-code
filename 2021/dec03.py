input_file = open('input03.txt', 'r')
allBits = input_file.readlines()

oneCounts = [0] * (len(allBits[0])-1)

gamma = 0
epsilon = 0

for bits in allBits:
    for i in range(0,len(bits)):
        if bits[i] == '1':
            oneCounts[i] += 1

print('--- Part One ---')

oneCountsReversed = oneCounts[::-1]

for i in range(0,len(oneCountsReversed)):
    if oneCountsReversed[i] > len(allBits)/2:
        gamma += 2**i
    else:
        epsilon += 2**i

print(gamma*epsilon)

print('--- Part Two ---')

def filter_func(bit, index, bits, counts):
    if bits[index] == bit:
        return True

    for i in range(index+1, len(counts)):
        if bits[i] == '1':
            counts[i] -= 1

    return False

o2Ratings = allBits
o2OneCounts = oneCounts.copy()
o2Rating = 0

co2Ratings = allBits
co2OneCounts = oneCounts
co2Rating = 0

index = 0
while len(o2Ratings) > 1:
    bit = '1' if o2OneCounts[index] >= len(o2Ratings)/2.0 else '0'
    print(bit + " " + str(o2OneCounts[index]) + " " + str(len(o2Ratings)/2.0))
    o2Ratings = list(filter(lambda bits: filter_func(bit, index, bits, o2OneCounts), o2Ratings))
    if bit == '1':
        o2Rating += 2**(len(o2OneCounts)-1-index)
    index += 1

while index < len(o2OneCounts):
    if o2Ratings[0][index] == '1':
        o2Rating += 2**(len(o2OneCounts)-1-index)
    index += 1

index = 0
while len(co2Ratings) > 1:
    bit = '0' if co2OneCounts[index] >= len(co2Ratings)/2 else '1'
    co2Ratings = list(filter(lambda bits: filter_func(bit, index, bits, co2OneCounts), co2Ratings))
    if bit == '1':
        co2Rating += 2**(len(co2OneCounts)-1-index)
    index += 1

while index < len(co2OneCounts):
    if co2Ratings[0][index] == '1':
        co2Rating += 2**(len(co2OneCounts)-1-index)
    index += 1

print(o2Rating*co2Rating)
