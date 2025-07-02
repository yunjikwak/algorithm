import sys
input = sys.stdin.readline

A,B,C = map(int, input().split())

result = 0
for a in range(1000):
    sum_all = A*a
    if sum_all > C:
        break
    for b in range(1000):
        sum_all += B*b
        if sum_all > C:
            break
        result = max(result, sum_all)

print(result)
