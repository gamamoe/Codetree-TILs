import sys

def is_subsequence(s1, s2) -> bool:
    result = False

    for i in range(len(s1) - len(s2) + 1):
        if s1[i:i + len(s2)] == s2:
            return True

    return result

n1, n2 = [int(x) for x in sys.stdin.readline().split()]
sequence1 = [int(x) for x in sys.stdin.readline().split()]
sequence2 = [int(x) for x in sys.stdin.readline().split()]

print('Yes' if is_subsequence(sequence1, sequence2) else 'No')
