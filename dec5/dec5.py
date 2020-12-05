input_file = open('input.txt', 'r')
lines = input_file.readlines()


def get_decimal_value(line):
    decode = {'F': 0, 'B': 1, 'L': 0, 'R': 1}
    val = 0
    for i, char in enumerate(line):
        val += decode[char] * 2**(len(line)-1 - i)

    return val


highest_pass = 0
found_passes = []

for line in lines:
    cur_pass = get_decimal_value(line[0:7])*8 + get_decimal_value(line[7:-1])

    highest_pass = max(highest_pass, cur_pass)
    found_passes.append(cur_pass)

print('--- Part One ---')
print(highest_pass)

print('--- Part Two ---')
found_passes.sort()

i = found_passes[0]
index = 0

while index < len(found_passes):
    if found_passes[index+1] == i+2:
        print(i+1)
        break

    index += 1
    i = found_passes[index]
