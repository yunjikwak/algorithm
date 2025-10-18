N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

visited_row = [False] * (N+1)
visited_col = [False] * (N+1)
answer = []
result = 0

def choose(curr_num):
    global result
    
    if curr_num == N:
        result = max(result, sum(answer))
        return
    
    for i in range(N):
        if visited_row[i]:
            continue

        for j in range(N):
            if visited_col[j]:
                continue
            
            visited_row[i] = True
            visited_col[j] = True

            answer.append(arr[i][j])
            choose(curr_num+1)
            answer.pop()
            visited_row[i] = False
            visited_col[j] = False

choose(0)
print(result)