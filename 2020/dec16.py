input_file = open('input.txt', 'r')
lines = input_file.readlines()

field_ranges = {}
for line in lines[:lines.index('\n')]:
    field = line[:line.index(':')]
    range1 = line[line.index(':')+2:line.index(' or ')]
    range2 = line[line.index(' or ')+4:]

    ranges = []
    ranges.append(range(int(range1[:range1.index('-')]),
                        int(range1[range1.index('-')+1:])+1))

    ranges.append(range(int(range2[:range2.index('-')]),
                        int(range2[range2.index('-')+1:])+1))

    field_ranges[field] = ranges

valid_tickets = []
error_rate = 0
for line in lines[lines.index('nearby tickets:\n')+1:]:
    vals = list(map(lambda x: int(x), line.split(',')))

    all_matched = True
    for i in vals:
        matched = False
        for r in field_ranges.values():
            if i in r[0] or i in r[1]:
                matched = True
                break
        if not matched:
            all_matched = False
            error_rate += i

    if all_matched:
        valid_tickets.append(vals)

print('--- Part One ---')
print(error_rate)

print('--- Part Two ---')
index_fields = []
for i in range(len(valid_tickets[0])):
    index_fields.append(list(field_ranges.keys()))

for ticket in valid_tickets:
    for i in range(len(ticket)):
        for field in index_fields[i]:
            if (ticket[i] not in field_ranges[field][0]
               and ticket[i] not in field_ranges[field][1]):
                index_fields[i].remove(field)

found_fields = set()
while len(found_fields) < len(index_fields):
    for i in index_fields:
        if len(i) == 1 and i[0] not in found_fields:
            field = i[0]
            found_fields.add(field)

            for j in index_fields:
                if len(j) > 1 and field in j:
                    j.remove(field)

ticket = list(map(lambda x: int(x),
              lines[lines.index('your ticket:\n')+1].split(',')))

product = 1
for i in range(len(index_fields)):
    if 'departure' in index_fields[i][0]:
        product *= ticket[i]

print(product)
