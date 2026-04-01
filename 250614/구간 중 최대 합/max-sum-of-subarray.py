import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
for i in range(N - K + 1):
    max_val = 0
    for j in range(i, i + K):
        max_val += arr[j]

    ans = max(ans, max_val)

print(ans)