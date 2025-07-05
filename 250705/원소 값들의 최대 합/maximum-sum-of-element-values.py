import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for i in range(N):
    cur = arr[i]
    idx = arr[i]-1
    for _ in range(1, M):
        cur += arr[idx]
        idx = arr[idx]-1
    
    result = max(result, cur)

print(result)