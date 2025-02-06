import sys

answer = []
while (string := sys.stdin.readline().rstrip()) != 'END':
    answer.append(string[::-1])

print('\n'.join(answer))
