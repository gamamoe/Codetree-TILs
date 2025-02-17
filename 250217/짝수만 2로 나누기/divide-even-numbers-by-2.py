import sys

def divide_by_two_if_even_number(seq):
    for i in range(len(seq)):
        if seq[i] % 2 == 0:
            seq[i] //= 2
        
n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
divide_by_two_if_even_number(arr)
print(' '.join(str(x) for x in arr))
