N = int(input())
arr = list(map(int, input().split()))

cnt = N

def bt(idx, cur_cnt):
    global cnt

    if idx == N-1:
        cnt = min(cnt, cur_cnt)
        return
    
    for i in range(1, arr[idx]+1):
        if idx + i < N:
            bt(idx+i, cur_cnt+1)
    return

bt(0, 0)
if cnt == N:
    print(-1)
else:
    print(cnt)