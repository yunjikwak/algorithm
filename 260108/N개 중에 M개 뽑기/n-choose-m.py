N, M = map(int, input().split())
answer = []

def bt(num, cnt):
    if cnt == M:
        print(*answer)
        return
    
    if num > N: 
        return
    
    for i in range(num, N+1):
        answer.append(i)
        bt(i+1, cnt+1)
        answer.pop()
    return

bt(1, 0)