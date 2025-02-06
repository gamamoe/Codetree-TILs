import sys

answer = []
while (string := sys.stdin.readline().rstrip()) != '0':
    answer.append(string)

print(len(answer))
print('\n'.join(x for x in answer[::2]))
