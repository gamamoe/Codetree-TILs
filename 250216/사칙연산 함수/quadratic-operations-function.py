import sys

def compute(x: int, y: int, operator: str) -> str:
    if operator == '+':
        return f'{x} {operator} {y} = {x + y}'
    elif operator == '-':
        return f'{x} {operator} {y} = {x - y}'
    elif operator == '*':
        return f'{x} {operator} {y} = {x * y}'
    elif operator == '/':
        return f'{x} {operator} {y} = {x // y}'
    else:
        return 'False'

a, o, c = sys.stdin.readline().rstrip().split()
print(compute(int(a), int(c), o))
