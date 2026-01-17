N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
result = 0

def choose(idx, cur):
    global result
    if idx == N:
        result = max(result, cur)
        return

    for i in range(N):
        if visited[i]:
            continue
        
        visited[i] = True
        choose(idx+1, min(cur, arr[idx][i]))
        visited[i] = False
    
choose(0, 10000)
print(result)