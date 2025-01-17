import sys

n = int(sys.stdin.readline())
answer = []
for i in range(1, n + 1):
    space = ' ' * (n - i)
    stars = ' '.join('*' for _ in range(i))
    answer.append(f'{space}{stars}')

for i in range(n - 1, 0, -1):
    space = ' ' * (n - i)
    stars = ' '.join('*' for _ in range(i))
    answer.append(f'{space}{stars}')

print('\n'.join(answer))
