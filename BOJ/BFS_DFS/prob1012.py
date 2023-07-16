import sys
sys.setrecursionlimit(10 ** 6) # 파이썬은 재귀 깊이 제한 설정 필수!!!!!!!!!!!

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

T = int(input()) # 테스트 케이스
result = [0]*T

for t in range(T):
    M, N, K = map(int, input().split()) # 가로 세로 배추 개수
    graph = [[0]*M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1 # 가로 세로 반대
    
    for i in range(N):
        for j in range(M):
            if dfs(i, j) == True:
                result[t] += 1
                
for i in range(T):
    print(result[i])