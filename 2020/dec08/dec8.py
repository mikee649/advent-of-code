def exec_program(lines):
    executed_lines = set()
    acc = 0
    line_num = 0

    while line_num not in executed_lines:
        executed_lines.add(line_num)

        if line_num >= len(lines):
            return {'acc': acc, 'terminated': True}

        command = lines[line_num]

        if 'acc' in command:
            acc += int(command[command.index(' ')+1:])
            line_num += 1
        elif 'jmp' in command:
            line_num += int(command[command.index(' ')+1:])
        else:
            line_num += 1

    return {'acc': acc, 'terminated': False}


input_file = open('input.txt', 'r')
lines = input_file.readlines()

print('--- Part One ---')
print(exec_program(lines)['acc'])

print('--- Part Two ---')
for line_num in range(0, len(lines)):
    if 'jmp' in lines[line_num]:
        lines[line_num] = lines[line_num].replace('jmp', 'nop')

        exec_results = exec_program(lines)
        if exec_results['terminated']:
            print(exec_results['acc'])
            break

        lines[line_num] = lines[line_num].replace('nop', 'jmp')
    elif 'nop' in lines[line_num]:
        lines[line_num] = lines[line_num].replace('nop', 'jmp')

        exec_results = exec_program(lines)
        if exec_results['terminated']:
            print(exec_results['acc'])
            break

        lines[line_num] = lines[line_num].replace('jmp', 'nop')
