import sys

n = int(sys.stdin.readline())
answer = 'pass' if n >= 80 else f'{80 - n} more score'
print(answer)
