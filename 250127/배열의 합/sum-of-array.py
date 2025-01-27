import sys

answer = []
for _ in range(4):
    answer.append(str(sum(int(x) for x in sys.stdin.readline().split())))

print('\n'.join(answer))
