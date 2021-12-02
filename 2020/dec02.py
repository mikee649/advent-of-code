import re

input_file = open('input.txt', 'r')
lines = input_file.readlines()

print('--- Part One ---')

count = 0

for line in lines:
    lower = int(line[0:line.index('-')])
    upper = int(line[line.index('-')+1:line.index(' ')])
    letter = line[line.index(' ')+1]
    password = line[line.index(':')+2:-1]

    num_matches = len(re.findall(letter, password))

    if num_matches >= lower and num_matches <= upper:
        count += 1

print(count)

print('--- Part Two ---')

count = 0

for line in lines:
    pos1 = int(line[0:line.index('-')])-1
    pos2 = int(line[line.index('-')+1:line.index(' ')])-1
    letter = line[line.index(' ')+1]
    password = line[line.index(':')+2:-1]

    matches = 1 if password[pos1] == letter else 0
    matches += 1 if password[pos2] == letter else 0

    if matches == 1:
        count += 1

print(count)
