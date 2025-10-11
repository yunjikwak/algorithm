N, M = map(int, input().split())

arr = []
def bt(cur_num, cnt):
    if cnt == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(cur_num+1, N+1):
        arr.append(i)
        bt(i, cnt+1)
        arr.pop()
    return

bt(0, 0)