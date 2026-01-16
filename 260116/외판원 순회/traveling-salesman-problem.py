N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
result = 10000*N

def choose(row, cnt, cur):
    global result

    if cnt == N-1:
        if arr[row][0] != 0: 
            result = min(result, cur + arr[row][0])
        return

    for i in range(1, N):
        if visited[i]:
            continue
        if arr[row][i] == 0:
            continue
        visited[i] = True
        choose(i, cnt+1, cur+arr[row][i])
        visited[i] = False
    
choose(0, 0, 0)
print(result)