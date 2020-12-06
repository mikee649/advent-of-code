input_file = open('input.txt', 'r')
lines = input_file.readlines()

print('--- Part One ---')
count = 0

questions = set()
for line in lines:
    if line == '\n':
        count += len(questions)
        questions = set()
        continue

    for char in line.replace('\n', ''):
        questions.add(char)

count += len(questions)

print(count)

print('--- Part Two ---')
count = 0

questions = None
for line in lines:
    if line == '\n':
        count += len(questions)
        questions = None
        continue

    if questions is None:
        questions = line.replace('\n', '')
        continue

    new_questions = ''
    for q in questions:
        if q in line:
            new_questions += q

    questions = new_questions

count += len(questions)
print(count)
