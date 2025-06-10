import sys
input = sys.stdin.readline

N = int(input())
arr = list(input().strip())

cnt = 0
for i in range(N):
    if arr[i] != 'C':
        continue
    for j in range(i, N):
        if arr[j] != 'O':
            continue
        for k in range(j, N):
            if arr[k] != 'W':
                continue
            else:
                cnt += 1
print(cnt)