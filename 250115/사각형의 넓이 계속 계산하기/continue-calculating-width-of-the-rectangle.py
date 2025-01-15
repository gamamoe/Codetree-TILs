import sys

answer = []
while True:
    width, height, char = sys.stdin.readline().rstrip().split()

    answer.append(str(int(width) * int(height)))
    if char == 'C':
        break

print('\n'.join(answer))
