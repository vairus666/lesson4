# Решение примеров, используя польскую запись
import re
import operator

OPERATORS = {
    '+': int.__add__, 
    '-': int.__sub__,
    '*': int.__mul__,
    '/': int.__truediv__,
    '%': int.__mod__,
    '^': int.__pow__,
}

PRIORITY = {1: ['+', '-'], 2: ['*', '/', '%', '^']}

def priority(value: str) -> int:
    for k, v in PRIORITY.items():
        if value in v:
            return k
    return -1
 
 
def pol_notation(expr: str) -> str:
    result = []
    stack = []
    for element in expr:
        if element not in OPERATORS.keys():
            result.append(element)
        else:
            last = stack[-1] if stack else None
            while priority(last) >= priority(element):
                result.append(stack.pop())
                last = stack[-1] if stack else None
            stack.append(element)
    for e in reversed(stack):
        result.append(e)
    return result


def polsh_math(srt):
    stack = []
    lst = list(srt)
    for i in srt:
        if i.isdigit():
            stack.append(i)
            lst.remove(i)
        else:
            cnt1 = stack.pop()
            cnt2 = stack.pop()
            stack.append(OPERATORS[i](int(cnt2), int(cnt1)))
            lst.remove(i)
    return stack.pop()

# str1 = ['4','+','5','*','10']
str1 = input('Vvedite simvoli cherez probel\n')
str2 = re.split(r'\s', str1)
str2 = pol_notation(str2)
print(str2)
print(polsh_math(str2))

