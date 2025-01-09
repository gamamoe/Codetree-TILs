import sys

if avg := float(sys.stdin.readline()) >= 1.0:
    print('High')
elif avg >= 0.5:
    print('Middle')
else:
    print('Low')
