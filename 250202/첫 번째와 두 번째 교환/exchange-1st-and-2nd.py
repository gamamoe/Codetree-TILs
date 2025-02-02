import sys

string = sys.stdin.readline().rstrip()
char1 = string[0]
char2 = string[1]

answer = []
for char in string:
    if char == char1:
        answer.append(char2)
    elif char == char2:
        answer.append(char1)
    else:
        answer.append(char)

print(''.join(answer))
