import re
import string


def eval_l2r(parsing_index, expression):
    result = 0
    current_op = '+'

    i = parsing_index

    while i < len(expression):
        if expression[i].isdigit():
            val = ''
            while i < len(expression) and expression[i].isdigit():
                val += expression[i]
                i += 1

            val = int(val)

            if current_op == '+':
                result += val
            else:
                result *= val
        elif expression[i] == '*':
            current_op = '*'
            i += 1
        elif expression[i] == '+':
            current_op = '+'
            i += 1
        elif expression[i] == '(':
            sub_expression = eval_l2r(i+1, expression)

            if current_op == '+':
                result += sub_expression['result']
            else:
                result *= sub_expression['result']

            i = sub_expression['parsing_index']
        elif expression[i] == ')':
            i += 1
            break

    return {'parsing_index': i, 'result': result}


def eval_with_plus_priority(expr):
    changes_made = True
    while changes_made:
        changes_made = False

        m = re.search("[0-9]+\\+[0-9]+", expr)

        if m:
            plus = m.group().index('+')
            term = int(m.group()[:plus]) + int(m.group()[plus+1:])
            expr = expr[:m.span()[0]] + str(term) + expr[m.span()[1]:]
            changes_made = True

        m = re.search('\\([0-9]+(\\*[0-9]+)*\\)', expr)

        if m:
            term = eval_l2r(0, m.group())['result']
            expr = expr[:m.span()[0]] + str(term) + expr[m.span()[1]:]
            changes_made = True

    return eval_l2r(0, expr)['result']


input_file = open('input.txt', 'r')
expressions = input_file.readlines()

print('--- Part One ---')
total = 0
for e in expressions:
    stripped_expr = e.translate({ord(c): None for c in string.whitespace})
    total += eval_l2r(0, stripped_expr)['result']

print(total)

print('--- Part Two ---')
total = 0
for e in expressions:
    stripped_expr = e.translate({ord(c): None for c in string.whitespace})
    total += eval_with_plus_priority(stripped_expr)

print(total)
