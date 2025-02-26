import collections
import sys


def has_more_than_two(s: str) -> str:
    return 'Yes' if len(collections.Counter(s)) >= 2 else 'No'

string = sys.stdin.readline().rstrip()
print(has_more_than_two(string))
