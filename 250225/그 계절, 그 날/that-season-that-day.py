import sys

def is_leap_year(y: int) -> bool:
    return y % 4 == 0 or (y % 4 == 0 and y % 100 == 0 and y % 400 == 0)


def print_season(y: int, m: int, d: int) -> str:
    last_day_by_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    if is_leap_year(y):
        last_day_by_month[2] += 1
    
    if last_day_by_month[m] < d:
        return '-1'
    
    if m in {3, 4, 5}:
        return 'Spring'
    elif m in {6, 7, 8}:
        return 'Summer'
    elif m in {9, 10, 11}:
        return 'Fall'
    else:
        return 'Winter'

year, month, day = [int(x) for x in sys.stdin.readline().split()]
print(print_season(year, month, day))