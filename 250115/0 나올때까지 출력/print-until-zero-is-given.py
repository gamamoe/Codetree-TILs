import sys

answer = []
while (num := int(sys.stdin.readline())) != 0:
    answer.append(str(num))

print('\n'.join(answer))
