import sys
sys.setrecursionlimit(1000)

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)] # 0번 인덱스 비우기

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False]*(N+1)
cnt = 0

def dfs(v):
    global cnt # 선언해야 함수 내에서 변경 가능!!
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(i)
   
dfs(1)
print(cnt)