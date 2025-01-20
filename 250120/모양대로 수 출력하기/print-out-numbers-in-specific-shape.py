import sys

n = int(sys.stdin.readline())
answer = []
for i in range(n, 0, -1):
    spaces = ' ' * (2 * (n - i))
    sequences = ' '.join(str(x) for x in range(i, 0, -1))
    answer.append(f'{spaces}{sequences}')

print('\n'.join(answer))
