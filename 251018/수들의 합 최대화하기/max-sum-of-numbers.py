N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

visited_col = [False] * (N+1)
answer = []
result = 0

def choose(row_idx):
    global result

    if row_idx == N:
        result = max(result, sum(answer))
        return
    
    for i in range(N):
        if visited_col[i]:
            continue
            
        visited_col[i] = True
        answer.append(arr[row_idx][i])
        choose(row_idx+1)
        answer.pop()
        visited_col[i] = False

choose(0)
print(result)