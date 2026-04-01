import sys
input = sys.stdin.readline

A,B,C = map(int, input().split())

result = 0
for a in range(1000):
    cur = A*a
    if cur > C:
        break
    for b in range(1000):
        sum_all = cur + B*b
        if sum_all > C:
            break
        result = max(result, sum_all)

print(result)
