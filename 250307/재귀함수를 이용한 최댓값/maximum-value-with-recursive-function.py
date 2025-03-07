import sys

def solution(arr, index, num_elements) -> int:
    if index == num_elements - 1:
        return arr[index]

    return max(arr[index], solution(arr, index + 1, num_elements))

n = int(sys.stdin.readline())
seq = [int(x) for x in sys.stdin.readline().split()]
print(solution(seq, 0, n))