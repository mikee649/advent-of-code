input_file = open('input04.txt', 'r')
lines = input_file.readlines()

def normalize_line(line):
    return line.lstrip().replace(' 0', '0.0000001').replace('  ', ' ')

nums = list(map(lambda x: int(x), normalize_line(lines[0]).split(',')))

boards = []
row = 0
for line in lines[1:]:
    if line == '\n':
        boards.append({'won': False, 'row_sums': [0]*5, 'col_sums': [0]*5, 'nums': {}})
        row = 0
    else:
        for col, val in enumerate(list(map(lambda x: float(x), normalize_line(line).split(' ')))):
            boards[-1]['row_sums'][row] += val
            boards[-1]['col_sums'][col] += val
            boards[-1]['nums'][val] = (row,col)
        row += 1


first = None
last = 0
for num in nums:
    for board in boards:
        if num in board['nums'] and not board['won']:
            board['row_sums'][board['nums'][num][0]] -= num
            if board['row_sums'][board['nums'][num][0]] == 0:
                score = int(sum(board['row_sums']) * num)
                first = first or score
                last = score
                board['won'] = True
            board['col_sums'][board['nums'][num][1]] -= num
            if board['col_sums'][board['nums'][num][1]] == 0:
                score = int(sum(board['col_sums']) * num)
                first = first or score
                last = score
                board['won'] = True

print('--- Part One ---')
print(first)
print('--- Part Two ---')
print(last)
