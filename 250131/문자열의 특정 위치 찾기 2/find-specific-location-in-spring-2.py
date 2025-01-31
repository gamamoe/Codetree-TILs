import sys

char = sys.stdin.readline().rstrip()
strings = [
    'apple',
    'banana',
    'grape',
    'blueberry',
    'orange',
]

answer = []
for string in strings:
    if string[2] == char or string[3] == char:
        answer.append(string)

answer.append(str(len(answer)))
print('\n'.join(answer))
