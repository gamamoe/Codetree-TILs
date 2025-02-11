import sys

def is_answer(n: str) -> str:
    return 'Yes' if int(n[0]) % 2 == 0 and (int(n[0]) + int(n[1])) % 5 == 0 else 'No'

n = sys.stdin.readline().rstrip()
print(is_answer(n))
