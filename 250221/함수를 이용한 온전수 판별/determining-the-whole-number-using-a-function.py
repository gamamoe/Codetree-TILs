import sys


def count_satisfied_nums(start: int, end: int) -> int:
    result = 0
    for num in range(start, end + 1):
        if num % 2 == 0 or str(num)[-1] == '5' or (num % 3 == 0 and num % 9 != 0):
            continue
        result += 1

    return result

a, b = [int(x) for x in sys.stdin.readline().split()]

print(count_satisfied_nums(a, b))
