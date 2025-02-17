import sys

def is_palindrome(s: str) -> str:
    return 'Yes' if s == s[::-1] else 'No'

string = sys.stdin.readline().rstrip()
print(is_palindrome(string))
