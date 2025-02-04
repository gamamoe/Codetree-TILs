import sys

chars = sys.stdin.readline().rstrip()
answer = []
for char in chars:
    if char.islower():
        answer.append(char.upper())
    elif char.isupper():
        answer.append(char.lower())

print(''.join(answer))
