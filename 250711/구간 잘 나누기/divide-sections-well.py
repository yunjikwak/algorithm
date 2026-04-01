import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = list(map(int, input().split()))

start = max(arr)
end = sum(arr)

for standard in range(start, end+1):
    cnt = 1
    internal_sum = 0
    for a in arr:
        internal_sum += a
        if internal_sum <= standard:
            continue
        internal_sum = a
        cnt += 1
    if cnt <= M:
        print(standard)
        break