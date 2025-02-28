import sys

def do_something(target, seq):
    answer = 0

    while True:
        answer += seq[target - 1]
        if target == 1:
            break
        if target % 2 == 0:
            target //= 2
        else:
            target -= 1
    return answer


n, m = [int(x) for x in sys.stdin.readline().split()]
sequence = [int(x) for x in sys.stdin.readline().split()]
print(do_something(m, sequence))
