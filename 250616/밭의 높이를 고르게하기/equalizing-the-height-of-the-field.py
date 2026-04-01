import sys
input = sys.stdin.readline

MAXSYS = sys.maxsize

N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

result = MAXSYS
for i in range(N-T+1):
    cost = 0
    for j in range(i, i+T):
        cost += abs(H - arr[j])
    result = min(result, cost)

print(result)