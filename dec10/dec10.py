input_file = open('input.txt', 'r')
lines = input_file.readlines()

print('--- Part One ---')
adapters = list(map(lambda line: int(line), lines))
adapters.sort()
adapters.insert(0, 0)
adapters.append(adapters[-1]+3)

delta1_count, delta3_count = 0, 0

i = 0
while i < len(adapters) - 1:
    if adapters[i+1] - adapters[i] == 1:
        delta1_count += 1
    elif adapters[i+1] - adapters[i] == 3:
        delta3_count += 1

    i += 1

print(delta1_count * delta3_count)

print('--- Part Two ---')
adapters.pop(0)
adapters.pop(-1)

arrangments = {0: 1}

for i in adapters:
    count = arrangments.get(i-1, 0)
    count += arrangments.get(i-2, 0)
    count += arrangments.get(i-3, 0)

    arrangments[i] = count

print(arrangments[adapters[-1]])
