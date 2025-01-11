import sys

year = int(sys.stdin.readline())

if year % 4 != 0 or (year % 4 == 0 and year % 100 == 0 and year % 400 != 0):
    print('false')
else:
    print('true')