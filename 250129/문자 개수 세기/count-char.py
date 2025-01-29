import sys

string = sys.stdin.readline().rstrip()
char = sys.stdin.readline().rstrip()
answer = 0
for c in string:
    if c == char:
        answer += 1

print(answer)