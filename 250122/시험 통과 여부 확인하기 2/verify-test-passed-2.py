import sys

num_of_students = int(sys.stdin.readline())
answer = 0
for _ in range(num_of_students):
    scores = [int(x) for x in sys.stdin.readline().split()]
    avg = sum(scores) / len(scores)

    if avg >= 60:
        print('pass')
        answer += 1
    else:
        print('fail')
    
print(answer)
