import sys
sys.setrecursionlimit(10000)
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)] # 0번 인덱스 비우기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(N+1): # N이 아니라 N+1!!!!!!
    graph[i].sort()
    
visited = [False]*(N+1)

def dfs(v):
	visited[v] = True
	print(v, end=' ')
	for i in graph[v]:
		if not visited[i]:
			dfs(i)

def bfs(start):
	queue = deque([start])
	visited[start] = True
	while queue :
		v = queue.popleft()
		print(v, end=' ')
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

dfs(V)
print()
visited = [False]*(N+1)
bfs(V)