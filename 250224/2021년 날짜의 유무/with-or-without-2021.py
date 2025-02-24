import sys

def is_exist_date(m: int, d: int) -> str:
    if m > 12:
        return 'No'
    
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

    if d > last_day_by_month[m]:
        return 'No'
    
    return 'Yes'


month, day = [int(x) for x in sys.stdin.readline().split()]
print(is_exist_date(month, day))
