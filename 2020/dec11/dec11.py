def look_direction(lines, row, col, direction, limit):
    row2, col2 = row + direction[0], col + direction[1]

    while row2 in range(0, len(lines)) and col2 in range(0, len(lines[0])):
        if lines[row2][col2] == 'L':
            return (row2, col2)
        if limit:
            return None

        row2 += direction[0]
        col2 += direction[1]

    return None


def construct_neighbor_map(lines, limit):
    neighbor_map = {}

    for row in range(0, len(lines)):
        for col in range(0, len(lines[0])):
            neighbors = []

            directions = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1),
                          (-1, 0), (-1, 1), (-1, -1)]

            for direction in directions:
                neighbors.append(look_direction(lines, row, col,
                                 direction, limit))

            neighbor_map[(row, col)] = list(filter(lambda n: n, neighbors))

    return neighbor_map


def full_seats_equilibrium(lines, neighbor_map, max_neighbors):
    num_rows, num_cols = len(lines), len(lines[0])

    prev_gen = {}

    for row in range(0, num_rows):
        for col in range(0, num_cols):
            if lines[row][col] == 'L':
                prev_gen[(row, col)] = 'L'

    while True:
        next_gen = {}
        full_count = 0
        for row, col in list(prev_gen.keys()):
            count = 0
            for n in neighbor_map[row, col]:
                if prev_gen[(n[0], n[1])] == '#':
                    count += 1

            if prev_gen[row, col] == 'L' and count == 0:
                seat = '#'
            elif prev_gen[row, col] == '#' and count > max_neighbors:
                seat = 'L'
            else:
                seat = prev_gen[row, col]

            next_gen[row, col] = seat

            full_count += 1 if seat == '#' else 0

        if next_gen == prev_gen:
            break

        prev_gen = next_gen

    return full_count


input_file = open('input.txt', 'r')
lines = list(map(lambda line: line.replace('\n', ''), input_file.readlines()))

print('--- Part One ---')
print(full_seats_equilibrium(lines, construct_neighbor_map(lines, True), 3))

print('--- Part Two ---')
print(full_seats_equilibrium(lines, construct_neighbor_map(lines, False), 4))
