N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited_r = [False] * N
visited_c = [False] * N

result = 0
def choose(cnt, cur):
    global result

    if cnt == N+1:
        result = max(result, cur)
        return

    for i in range(N):
        if visited_r[i]:
            continue
        
        for j in range(N):
            if visited_c[j]:
                continue
            
            visited_r[i] = True
            visited_c[j] = True
            choose(cnt+1, cur+arr[i][j])
            visited_r[i] = False
            visited_c[j] = False

choose(1, 0)
print(result)