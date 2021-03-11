PRIORITY = {1: ['+', '-'], 2: ['*', '/']}

def priority(value: str) -> int:
    for k, v in PRIORITY.items():
        if value in v:
            return k
    return -1
 
 
def pol_notation(expr: str) -> str:
    result = []
    stack = []
    for element in expr:
        if element not in '+-*/':
            result.append(element)
        else:
            last = None if not stack else stack[-1]
            while priority(last) >= priority(element):
                result.append(stack.pop())
                last = None if not stack else stack[-1]
            stack.append(element)
    for e in reversed(stack):
        result.append(e)
    return ''.join(result)

import operator

OPERATORS = {
    '+': int.__add__, 
    '-': int.__sub__,
    '*': int.__mul__,
    '/': int.__truediv__,
    '%': int.__mod__,
    '^': int.__pow__,
}

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

str1 = input('Primer')
str1 = pol_notation(str1)
print(str1)
print(polsh_math(str1))
