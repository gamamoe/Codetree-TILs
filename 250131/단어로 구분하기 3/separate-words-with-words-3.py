import sys

strings = sys.stdin.readline().rstrip().split()
answer = []
for string in strings[::-1]:
    answer.append(string)

print('\n'.join(answer))
