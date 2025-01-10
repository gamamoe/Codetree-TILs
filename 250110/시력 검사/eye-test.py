import sys

a = float(sys.stdin.readline())
b = float(sys.stdin.readline())

if a >= 1.0 and b >= 1.0:
    print('High')
elif a >= 0.5 and b >= 0.5:
    print('Middle')
else:
    print('Low')
