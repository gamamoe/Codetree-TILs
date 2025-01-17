import sys

n = int(sys.stdin.readline())
answer = []
for i in range(2 * n + 1):
    if i % 2 == 0:
        answer.append(' '.join('*' for _ in range(2 * n + 1)))
    else:
        answer.append('   '.join('*' for _ in range(n + 1)))

print('\n'.join(answer))
