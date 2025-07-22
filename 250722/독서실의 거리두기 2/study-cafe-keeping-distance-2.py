import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().strip()))
pos = [i for i, v in enumerate(arr) if v == 1]

min_max = 0
for p in range(1, len(pos)):
    diff = pos[p] - pos[p-1]
    if min_max*2 < diff:
        tmp = diff // 2
        min_max = tmp

if arr[N-1] == 0:
    min_max = max(min_max, N-1-pos[-1])

print(min_max)