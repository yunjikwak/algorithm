N = int(input())
visited = [False] * (N+1)

result = []

def choose(cnt):
    if cnt == N+1:
        print(*result)
        return

    for i in range(N, 0, -1):
        if visited[i]:
            continue
        
        visited[i] = True
        result.append(i)
        choose(cnt+1)
        result.pop()
        visited[i] = False
    

choose(1)