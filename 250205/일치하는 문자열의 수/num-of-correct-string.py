import sys

n, string = sys.stdin.readline().rstrip().split()
answer = 0
for _ in range(int(n)):
    current_string = sys.stdin.readline().rstrip()

    if string == current_string:
        answer += 1

print(answer)
