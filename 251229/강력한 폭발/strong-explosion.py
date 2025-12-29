N = int(input())
bomb = [[]]
bomb.append([[-2, -1, 1, 2], [0, 0, 0, 0]])
bomb.append([[-1, 0, 1, 0], [0, 1, 0, -1]])
bomb.append([[-1, -1, 1, 1], [-1, 1, 1, -1]])

# board = [list(map(int, input().split())) for _ in range(N)]
board = []
candidate = []
for i in range(N):
    cur = list(map(int, input().split()))
    for idx, num in enumerate(cur):
        if num == 1:
            candidate.append((i, idx))
    board.append(cur)

def calculate(arr):
    cur = [row[:] for row in board]

    for idx in range(len(arr)):
        dx = bomb[arr[idx]][0]
        dy = bomb[arr[idx]][1]
        a, b = candidate[idx]

        for d in range(4):
            nx, ny = a+dx[d], b+dy[d]
            if nx >= 0 and nx < N and ny >= 0 and ny < N and cur[nx][ny] == 0:
                cur[nx][ny] += 1
    
    val = 0
    for i in range(N):
        for j in range(N):
            if cur[i][j] == 1:
                val += 1
    return val

arr = []
result = 0
def back(cur_idx):
    global result
    
    if len(arr) == len(candidate):
        result = max(result, calculate(arr))
        return
    
    for i in range(1, 4):
        arr.append(i)
        back(cur_idx+1)
        arr.pop()
    
    return

back(0)
print(result)