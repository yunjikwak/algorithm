import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

total = sum(arr)
result = S
for i in range(N):
    for j in range(i+1, N):
        cur = total - arr[i] - arr[j]
        if result > abs(S - cur):
            result = abs(S - cur)

print(result)