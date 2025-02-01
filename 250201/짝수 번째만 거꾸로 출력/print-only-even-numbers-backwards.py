import sys

string = sys.stdin.readline().rstrip()
answer = []
for index, char in enumerate(string):
    if index % 2 == 1:
        answer.append(char)

print(''.join(answer[::-1]))
