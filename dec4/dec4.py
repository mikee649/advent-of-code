import re


def is_valid(key, value):
    if(key == 'byr'):
        if 1920 <= int(value) <= 2002:
            return True
    elif(key == 'iyr'):
        if 2010 <= int(value) <= 2020:
            return True
    elif(key == 'eyr'):
        if 2020 <= int(value) <= 2030:
            return True
    elif(key == 'hgt'):
        if value[-2:] == 'cm':
            if 150 <= int(value[:-2]) <= 193:
                return True
        elif value[-2:] == 'in':
            if 59 <= int(value[:-2]) <= 76:
                return True
    elif(key == 'hcl'):
        if re.search("#([0-9]|[a-f]){6}$", value):
            return True
    elif(key == 'ecl'):
        if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return True
    elif key == 'pid':
        if re.search("^[0-9]{9}$", value):
            return True

    return False


def count_valid_passports(lines, check_values):
    valid_count = 0

    unvalidated_keys = REQUIRED_KEYS.copy()
    for line in lines:
        if line == '\n':
            if len(unvalidated_keys) == 0:
                valid_count += 1

            unvalidated_keys = REQUIRED_KEYS.copy()
            continue

        pairs = list(map(lambda pair: pair.replace('\n', ''), line.split(' ')))

        valid_keys = []

        for pair in pairs:
            key = pair[0:pair.index(':')]
            value = pair[pair.index(':')+1:]

            if not check_values or is_valid(key, value):
                valid_keys.append(key)

        unvalidated_keys = [key for key in unvalidated_keys
                            if key not in valid_keys]

    if len(unvalidated_keys) == 0:
        valid_count += 1

    return valid_count


input_file = open('input.txt', 'r')
lines = input_file.readlines()

REQUIRED_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

print('--- Part One ---')
print(count_valid_passports(lines, False))
print('--- Part Two ---')
print(count_valid_passports(lines, True))
