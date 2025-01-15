import sys

n = int(sys.stdin.readline())
current = 1
count = 0
while True:
    if current == n:
        print(count)
        break

    current *= 2
    count += 1
    