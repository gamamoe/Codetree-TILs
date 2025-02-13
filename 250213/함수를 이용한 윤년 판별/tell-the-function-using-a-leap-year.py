import sys

def is_leap_year(y: int) -> str:
    if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
        return 'false'
    else:
        return 'true'

year = int(sys.stdin.readline())
print(is_leap_year(year))
