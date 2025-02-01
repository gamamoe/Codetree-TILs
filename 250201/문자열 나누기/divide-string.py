import sys

n = int(sys.stdin.readline())
string = ''.join(sys.stdin.readline().rstrip().split())
answer = []

for i in range(0, len(string), 5):
    answer.append(string[i:i + 5])

print('\n'.join(answer))
