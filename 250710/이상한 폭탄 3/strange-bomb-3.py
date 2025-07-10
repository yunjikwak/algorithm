import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bomb = list(int(input()) for _ in range(N))

max_num = 0
max_cnt = 0
for i in range(N-K):
    cnt = 1
    num = bomb[i]
    for j in range(1, K+1):
        if num == bomb[i+j]:
            cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
        max_num = num
    elif cnt == max_cnt:
        max_num = max(max_num, num)
print(max_num)