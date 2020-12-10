def has_sum_combo(target, nums):
    checked_lines = set()

    for num in nums:
        if target-num != num and target-num in checked_lines:
            return True

        checked_lines.add(num)

    return False


input_file = open('input.txt', 'r')
lines = input_file.readlines()

print('--- Part One ---')
prev = []

for line in lines[:25]:
    prev.append(int(line))

for line in lines[26:]:
    if not has_sum_combo(int(line), prev):
        invalid_num = int(line)
        break

    prev.pop(0)
    prev.append(int(line))

print(invalid_num)

print('--- Part Two ---')
start = 0
end = 1
cur_sum = int(lines[0]) + int(lines[1])

while end < len(lines):
    if cur_sum == invalid_num:
        nums = list(map(lambda line: int(line), lines[start:end+1]))
        print(min(nums) + max(nums))
        break
    elif cur_sum > invalid_num:
        cur_sum -= int(lines[start])
        start += 1
    else:
        end += 1
        cur_sum += int(lines[end])
