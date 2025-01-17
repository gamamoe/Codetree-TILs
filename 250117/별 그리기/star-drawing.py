import sys

n = int(sys.stdin.readline())
answer = []
for i in range(1, n + 1):
    space = ' ' * (n - i)
    stars = '*' * (2 * i - 1)
    answer.append(f'{space}{stars}')

for i in range(n - 1, 0, -1):
    space = ' ' * (n - i)
    stars = '*' * (2 * i - 1)
    answer.append(f'{space}{stars}')

print('\n'.join(answer))
