import sys

a, b = sys.stdin.readline().rstrip().split()

new_a = []
for char in a:
    if char.isdigit():
        new_a.append(char)
    else:
        break

new_b = []
for char in b:
    if char.isdigit():
        new_b.append(char)
    else:
        break

new_a = int(''.join(new_a))
new_b = int(''.join(new_b))
print(new_a + new_b)
