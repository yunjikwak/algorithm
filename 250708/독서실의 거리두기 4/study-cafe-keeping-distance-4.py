import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().strip()))

def distance(lst):
    dis = N

    last = -1
    for i in range(len(lst)):
        if lst[i] == 1:
            if last != -1:
                dis = min(dis, i-last)
            last = i
    return dis

result = 0
for i in range(N):
    if arr[i] != 0:
        continue
    for j in range(i+1, N):
        if arr[j] != 0:
            continue
        arr[i] = 1
        arr[j] = 1
        result = max(result, distance(arr))
        arr[i] = 0
        arr[j] = 0
print(result)