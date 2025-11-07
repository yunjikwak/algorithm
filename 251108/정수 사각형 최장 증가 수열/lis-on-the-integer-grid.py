import sys
sys.setrecursionlimit(250000)

N = int(sys.stdin.readline())

arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

dp = [[-1] * N for _ in range(N)]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 1
    
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        
        if in_range(nx, ny) and arr[nx][ny] > arr[x][y]:
            dp[x][y] = max(dp[x][y], 1 + dfs(nx, ny))
            
    return dp[x][y]

max_path = 0
for i in range(N):
    for j in range(N):
        max_path = max(max_path, dfs(i, j))

print(max_path)