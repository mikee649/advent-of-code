input_file = open('input.txt', 'r')
lines = input_file.readlines()

print('--- Part One ---')

checked_lines = set()

for line in lines:
    if (2020 - int(line)) in checked_lines:
        print(int(line) * (2020-int(line)))
        break

    checked_lines.add(int(line))

print('--- Part Two ---')

checked_lines = []
pairs = {}  # stores (a + b) -> (a*b)

for line in lines:
    if (2020 - int(line)) in pairs:
        print(int(line) * pairs[2020-int(line)])
        break

    for n in checked_lines:
        if n + int(line) not in pairs:
            pairs[n + int(line)] = int(line)*n
    checked_lines.append(int(line))
