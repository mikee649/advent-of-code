puzzle_input = '8,13,1,0,18,9'

nums = {}
for index, num in enumerate(puzzle_input.split(',')):
    nums[int(num)] = [index+1]
    last_num = int(num)

round_num = index + 2

while round_num <= 30000000:
    if len(nums[last_num]) < 2:
        diff = 0
    else:
        diff = nums[last_num][-1] - nums[last_num][-2]

    nums[diff] = (nums.get(diff, []) + [round_num])[-2:]
    last_num = diff

    round_num += 1

    if round_num == 2021:
        print('--- Part One ---')
        print(last_num)

print('--- Part Two ---')
print(last_num)
