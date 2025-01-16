import sys

n = int(sys.stdin.readline())
answer = []
for i in range(n, 0, -1):
    space = ' ' * (2 * (n - i))
    stars = ' '.join('*' for _ in range(2 * i - 1))
    answer.append(f'{space}{stars}')

print('\n'.join(answer))
