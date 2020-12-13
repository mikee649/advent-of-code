input_file = open('input.txt', 'r')
lines = input_file.readlines()

print('--- Part One ---')
earliest = int(lines[0])

chosen_bus = {'id': -1, 'wait': float('inf')}

for bus in lines[1].split(','):
    if bus == 'x':
        continue

    bus_id = int(bus)

    wait = int(int(earliest/bus_id + 1)*bus_id - earliest)

    if wait < chosen_bus['wait']:
        chosen_bus = {'id': bus_id, 'wait': wait}

print(chosen_bus['id'] * chosen_bus['wait'])

print('--- Part Two ---')
bus_list = lines[1].split(',')

busses = {}
for i in range(0, len(bus_list)):
    if not bus_list[i] == 'x':
        busses[int(bus_list[i])] = i

time = 0
incrementer = 1
for bus in busses:
    while not (time + busses[bus]) % bus == 0:
        time += incrementer
    incrementer *= bus

print(time)
