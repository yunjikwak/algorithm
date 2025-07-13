import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

result = sys.maxsize
for i in range(max(arr)):
    cost = 0
    for a in arr:
        if a < i:
            cost += abs(i-a)
        elif a > i+K:
            cost += abs(a-(i+K))
    result = min(result, cost)
print(result)