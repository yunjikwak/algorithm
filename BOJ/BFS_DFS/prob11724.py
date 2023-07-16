# python -> 시간 초과 / pypy3 -> 성공 ?????

import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split()) # 정점, 간선
graph = [[] for _ in range(N+1)] # 0번 인덱스 비우기

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False]*(N+1)

def dfs(v):
	visited[v] = True
	# 현재 노드와 연결된 다른 노드 재귀적으로 방문
	for i in graph[v]:
		if not visited[i]:
			dfs(i)

result = 0

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        result += 1

print(result)