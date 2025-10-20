N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

visited = [False] * N
answer = []
result = 0

def choose(curr_num):
    global result
    
    if curr_num == N:
        cur = min(answer)
        result = max(result, cur)

    for i in range(N):
        if visited[i]:
            continue
        
        visited[i] = True
        answer.append(arr[curr_num][i])
        choose(curr_num+1)
        answer.pop()
        visited[i] = False
    
    return

choose(0)
print(result)