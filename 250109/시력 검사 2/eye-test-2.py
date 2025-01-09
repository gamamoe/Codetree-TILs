import sys

avg = float(sys.stdin.readline())
if avg >= 1.0:
    print('High')
elif avg >= 0.5:
    print('Middle')
else:
    print('Low')
