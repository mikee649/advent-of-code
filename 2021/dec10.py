input_file = open('input10.txt', 'r')
lines = input_file.readlines()

match = {')': '(', ']': '[', '}': '{', '>': '<'}
scoreMapP1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
scoreMapP2 = {'(': 1, '[': 2, '{': 3, '<': 4}

scoreP1 = 0
scoresListP2 = []

for line in lines:
    stack = []
    for char in line.rstrip():
        if char in scoreMapP1:
            if stack.pop() != match[char]:
                scoreP1 += scoreMapP1[char]
                stack = []
                break
        else:
            stack.append(char)

    if len(stack) > 0:
        scoreP2 = 0
        for char in reversed(stack):
            scoreP2 *= 5
            scoreP2 += scoreMapP2[char]
        scoresListP2.append(scoreP2)

scoresListP2.sort()

print('--- Part One ---')
print(scoreP1)

print('--- Part Two ---')
print(scoresListP2[int(len(scoresListP2)/2)])
