import sys

answer = 0
for _ in range(2):
    string = sys.stdin.readline().rstrip()

    temp = []
    for char in string:
        if not char.isdigit():
            continue
        temp.append(char)
    answer += int(''.join(temp))

print(answer)
