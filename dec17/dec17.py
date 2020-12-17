input_file = open('input.txt', 'r')
lines = input_file.readlines()


def neighbors(cube, dimensions):
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for m in (range(-1, 2) if dimensions == 4 else [0]):
                    neighbors.append(
                            (cube[0]+i, cube[1]+j, cube[2]+k, cube[3]+m))

    neighbors.remove(cube)
    return neighbors


def next_gen_neighbor_count(cur_gen, dimensions):
    next_gen = {}
    for cube in cur_gen.keys():
        if cur_gen[cube] == '#':
            for n in neighbors(cube, dimensions):
                next_gen[n] = next_gen[n] + 1 if n in next_gen else 1

    return next_gen


def convert_count_to_state(gen, prev_gen):
    for cube in gen:
        prev_state = prev_gen[cube] if cube in prev_gen else '.'

        if prev_state == '#':
            gen[cube] = '#' if gen[cube] in [2, 3] else '.'
        else:
            gen[cube] = '#' if gen[cube] == 3 else '.'


def gen_six_active_count(dimensions):
    generation = {}

    for row, line in enumerate(lines):
        for col in range(len(line)-1):
            generation[(row, col, 0, 0)] = line[col]

    gen_round = 1
    while gen_round <= 6:
        next_gen = next_gen_neighbor_count(generation, dimensions)
        convert_count_to_state(next_gen, generation)
        generation = next_gen
        gen_round += 1

    return sum(state == '#' for state in generation.values())


print('--- Part One ---')
print(gen_six_active_count(3))

print('--- Part Two ---')
print(gen_six_active_count(4))
