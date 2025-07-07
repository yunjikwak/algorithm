import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(M)]

result = 0
for i in range(M):
    cnt = 1
    x, y = arr[i]
    for j in range(i+1, M):
        a, b = arr[j]
        if (x == a and y == b) or (x == b and y == a):
            cnt += 1
    result = max(result, cnt)
print(result) 