import sys
input = sys.stdin.readline

a = list(input().strip())
max_val = int(''.join(a), 2)

for i in range(len(a)):
    if a[i] == '1':
        a[i] = '0'
    else:
        a[i] = '1'

    val = int(''.join(a), 2)
    if max_val < val:
        max_val = val

    if a[i] == '1':
        a[i] = '0'
    else:
        a[i] = '1'

print(max_val)
