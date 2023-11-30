R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

alpha = set(board[0][0]) # 초기값 설정
result = 0

def dfs(x, y, cnt):
    global result
    result = max(result, cnt)
    
    if result == 26:
        return 26
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= R or ny < 0 or ny >= C or board[nx][ny] in alpha:
            continue
        alpha.add(board[nx][ny])
        dfs(nx, ny, cnt+1)
        alpha.remove(board[nx][ny])

dfs(0, 0, 1)
print(result)