input_file = open('input13.txt', 'r')
lines = input_file.readlines()

dots = set()

inputDivider = lines.index('\n')

folds = []

for line in lines[:inputDivider]:
    x, y = line.rstrip().split(',')
    dots.add((int(x), int(y)))
    
for line in lines[inputDivider+1:]:
    instruction, value = line.rstrip().split('=')
    folds.append((instruction[-1], int(value)))
    
toRemove = []
toAdd = []

for fold in folds:
    for dot in dots:
        if fold[0] == 'x' and dot[0] > fold[1]:
            newX = fold[1] - (dot[0] - fold[1])
            toAdd.append((newX, dot[1]))
            toRemove.append(dot)
        elif fold[0] == 'y' and dot[1] > fold[1]:
            newY = fold[1] - (dot[1] - fold[1])
            toAdd.append((dot[0], newY))
            toRemove.append(dot)
            
    for dot in toRemove:
        dots.remove(dot)
    toRemove = []

    for dot in toAdd:
        dots.add(dot)
    toAdd = []
    
    if fold == folds[0]:
        print('--- Part One ---')
        print(len(dots))

maxX = 0
maxY = 0
for dot in dots: 
    if dot[0] > maxX:
        maxX = dot[0]
    if dot[1] > maxY:
        maxY = dot[1]
        
print('--- Part Two ---')
for y in range(maxY+1):
    for x in range(maxX+1):
        if (x, y) in dots:
            print('#', end='')
        else:
            print(' ', end='')
    print()
