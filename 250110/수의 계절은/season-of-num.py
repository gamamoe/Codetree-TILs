import sys

month = int(sys.stdin.readline())
if 3 <= month <= 5:
    print('Spring')
elif 6 <= month <= 8:
    print('Summer')
elif 9 <= month <= 11:
    print('Fall')
else:
    print('Winter')
