N = int(input())
arr = list(map(int, input().split()))

answer = N*N
def bt(cur, cnt):
    global answer

    if cur == N-1:
        answer = min(answer, cnt)
    elif cur > N-1:
        return
        
    for i in range(1, arr[cur]+1):
        bt(cur+i, cnt+1)
    return

bt(0, 0)
if answer == N*N:
    print(-1)
else:
    print(answer)