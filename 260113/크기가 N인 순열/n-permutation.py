N = int(input())
visited = [False] * (N+1)
answer = []

def choose(curr_num):
    if curr_num == N + 1:
        print(*answer)
        return
    
    for i in range(1, N+1):
        if visited[i]:
            continue
        
        visited[i] = True
        answer.append(i)
        
        choose(curr_num + 1)

        answer.pop()
        visited[i] = False

choose(1)
