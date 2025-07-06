import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

max_cnt = 0
start = min(arr)
end = max(arr) + 1
for a in range(start, end):
    cnt = 0
    for elem in arr:
        if a <= elem and elem <= a + K:
            cnt += 1
        else:
            continue
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)