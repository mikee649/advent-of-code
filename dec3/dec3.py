input_file = open('input.txt', 'r')
rows = list(map(lambda row: row.replace('\n', ''), input_file.readlines()))


def count_trees(rows, down, right):
    row = 0
    col = 0

    trees_hit = 0

    while row < len(rows)-down:
        row += down
        col = (col + right) % len(rows[0])

        if rows[row][col] == '#':
            trees_hit += 1

    return trees_hit


print('--- Part One ---')

print(count_trees(rows, 1, 3))

print('--- Part Two ---')

slopes = [
    {'right': 1, 'down': 1},
    {'right': 3, 'down': 1},
    {'right': 5, 'down': 1},
    {'right': 7, 'down': 1},
    {'right': 1, 'down': 2},
]

product = 1

for slope in slopes:
    product *= count_trees(rows, slope['down'], slope['right'])

print(product)
