input_file = open('input06.txt', 'r')
fishies = input_file.readlines()[0]

states = [0]*9

for fish in fishies.split(','):
    states[int(fish)] += 1

for i in range(0,80):
    states.append(states.pop(0))
    states[6] += states[8]

print('--- Part One ---')
print(sum(states))

for i in range(80,256):
    states.append(states.pop(0))
    states[6] += states[8]

print('--- Part Two ---')
print(sum(states))
