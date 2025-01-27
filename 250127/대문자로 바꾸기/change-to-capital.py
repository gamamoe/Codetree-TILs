import sys

answer = []
for _ in range(5):
    answer.append(' '.join([char.upper() for char in sys.stdin.readline().rstrip().split()]))

print('\n'.join(answer))
