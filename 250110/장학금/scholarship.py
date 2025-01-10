import sys

mid_term_score, final_score = [int(x) for x in sys.stdin.readline().split()]
if mid_term_score < 90:
    print(0)
else:
    if final_score >= 95:
        print(100000)
    elif final_score >= 90:
        print(50000)
    else:
        print(0)
