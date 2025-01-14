import sys

n = int(sys.stdin.readline())
x = n
for divisor in range(1, n + 1):
    if (ret := x // divisor) > 1:
        x = ret
        continue
    else:
        print(divisor)
        break
