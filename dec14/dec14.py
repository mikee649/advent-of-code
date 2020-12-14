input_file = open('input.txt', 'r')
lines = input_file.readlines()

print('--- Part One ---')


def apply_value_mask(x, mask):
    xbin = '{0:036b}'.format(x)

    res = ''
    for i in range(0, 36):
        res += xbin[i] if mask[i] == 'X' else mask[i]

    return int(res, 2)


mem = {}
for line in lines:
    if 'mask' in line:
        mask = line[7:]
        continue

    key = line[line.index('[')+1:line.index(']')]

    mem[key] = apply_value_mask(int(line[line.index('=')+1:]), mask)

print(sum(list(mem.values())))

print('--- Part Two ---')


def apply_address_mask(x, mask):
    xbin = '{0:036b}'.format(x)

    xmask = ''
    for i in range(0, 36):
        xmask += xbin[i] if mask[i] == '0' else mask[i]

    addresses = []
    calculate_addresses(xmask, addresses)

    return addresses


def calculate_addresses(address, address_list):
    if 'X' not in address:
        address_list.append(int(address, 2))
        return

    calculate_addresses(address.replace('X', '0', 1), address_list)
    calculate_addresses(address.replace('X', '1', 1), address_list)


mem = {}
for line in lines:
    if 'mask' in line:
        mask = line[7:]
        continue

    key = int(line[line.index('[')+1:line.index(']')])

    val = int(line[line.index('=')+1:])

    addresses = apply_address_mask(key, mask)
    for address in addresses:
        mem[address] = val

print(sum(list(mem.values())))
