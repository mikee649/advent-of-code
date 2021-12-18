import re

input_file = open('input18.txt', 'r')
snailNums = list(map(lambda x: x.rstrip(), input_file.readlines()))


def add_to_last(string, val):
    matches = re.findall(r'\d+', string)

    if len(matches) == 0:
        return string

    splitNum = string.rsplit(matches[-1], 1)
    return splitNum[0] + str(int(matches[-1]) + val) + splitNum[1]


def add_to_first(string, val):
    matches = re.findall(r'\d+', string)

    if len(matches) == 0:
        return string

    splitNum = string.split(matches[0], 1)
    return splitNum[0] + str(int(matches[0]) + val) + splitNum[1]


def apply_split_val(string, val):
    first = int(val) // 2
    second = int(val) - first

    return string.replace(val, '[%s,%s]' % (first, second), 1)


def reduce(snailNum):
    prevNum = ''

    while prevNum != snailNum:
        prevNum = snailNum
        snailNum = ''
        depth = 0

        index = -1
        while index < len(prevNum) - 1:
            index += 1

            if prevNum[index] == ']':
                depth -= 1
                snailNum += ']'
                continue

            if prevNum[index] == '[':
                depth += 1

                if depth < 5:
                    snailNum += '['
                    continue

                # Explode
                pair = prevNum[index + 1:prevNum.index(']', index)].split(',')
                snailNum = add_to_last(snailNum, int(pair[0]))
                snailNum += '0'
                snailNum += add_to_first(prevNum[prevNum.index(']',
                                         index) + 1:], int(pair[1]))
                break

            snailNum += prevNum[index]

        # If there was an explosion check for more explosions
        if snailNum != prevNum:
            continue

        # Split large numbers
        nums = list(
            filter(
                lambda x: int(x) >= 10,
                re.findall(
                    r'\d+',
                    snailNum)))
        if len(nums) == 0:
            continue

        snailNum = apply_split_val(snailNum, nums[0])

    return snailNum


def add(num1, num2):
    return reduce('[%s,%s]' % (num1, num2))


def calculate_sum(snailNum):
    evalString = snailNum.replace(
        '[', '(3*').replace(',', '+2*').replace(']', ')')
    return eval(evalString)


finalNum = snailNums[0]

for snailNum in snailNums[1:]:
    finalNum = add(finalNum, snailNum)

print('--- Part One ---')
print(calculate_sum(finalNum))

maxSum = 0
for num1 in snailNums:
    for num2 in snailNums:
        if num1 == num2:
            continue

        maxSum = max(maxSum, calculate_sum(add(num1, num2)))

print('--- Part Two ---')
print(maxSum)
