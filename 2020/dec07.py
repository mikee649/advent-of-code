input_file = open('input.txt', 'r')
lines = input_file.readlines()

print('--- Part One ---')


def traverse_parents(key, bags, parent_set):
    if key not in bags:
        return

    for parent in bags[key]:
        if parent not in parent_set:
            parent_set.add(parent)
            traverse_parents(parent, bags, parent_set)


bags = {}

for line in lines:
    parent = line[:line.index(' bags')]

    children = line[line.index('bags contain')+12:].split(',')
    children = list(map(lambda child:
                    child[1:][child[1:].index(' ')+1:child[1:].index(' bag')],
                    children))

    for child in children:
        parents = bags.get(child, [])
        parents.append(parent)
        if child not in bags:
            bags[child] = parents

parent_set = set()
traverse_parents('shiny gold', bags, parent_set)

print(len(parent_set))

print('--- Part Two ---')


def count_bags(key, bags):
    if key not in bags:
        return 0

    count = 0

    for child in bags[key]:
        count += child[1] + child[1]*count_bags(child[0], bags)

    return count


bags = {}

for line in lines:
    parent = line[:line.index(' bags')]

    children = line[line.index('bags contain')+12:].split(',')
    children = list(map(lambda child:
                    child[1:][:child[1:].index(' bag')], children))

    if children == ['no other']:
        continue

    bags[parent] = []
    for child in children:
        bags[parent].append((child[child.index(' ')+1:],
                             int(child[:child.index(' ')])))

print(count_bags('shiny gold', bags))
