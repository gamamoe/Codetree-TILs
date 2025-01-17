import sys

n = int(sys.stdin.readline())
answer = []
for i in range(1, n + 1):
    space = ' ' * (2 * (n - i))
    chars = ' '.join('@' for _ in range(i))
    answer.append(f'{space}{chars}')

for i in range(n - 1, 0, -1):
    answer.append(' '.join('@' for _ in range(i)))

print('\n'.join(answer))
