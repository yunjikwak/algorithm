N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

visited = [False] * (N+1)
answer = []
result = 10000*100

def choose(cur_idx):
    global result
    if len(answer) == N-1:
        if visited[0] == True:
            return
        else:
            answer.append(arr[cur_idx][0])
            result = min(result, sum(answer))
        return
    
    for i in range(N):
        if visited[i] or arr[cur_idx][i] == 0:
            continue
        
        visited[i] = True
        answer.append(arr[cur_idx][i])
        choose(i)
        answer.pop()
        visited[i] = False
    
choose(0)
print(result)