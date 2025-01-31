import sys

strings = sys.stdin.readline().rstrip().split()
answer = []
for index, string in enumerate(strings):
    if index % 2 == 0:
        answer.append(string)

print('\n'.join(answer))
