import sys
sys.setrecursionlimit(10**4) # 이거 안 하면 런타임 에러남

# 노드의 수 N / 간선의 수 M / 시작 노드 K
N, M, K = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

visited = [False for _ in range(N+1)]

def dfs(v, node):
	visited[v] = True
	node += 1
	graph[v] = sorted(graph[v])
	for i in graph[v]:
		if not visited[i]:
			return dfs(i, node)
	else:
		return v, node
	
# dfs(K)
last, s_node = dfs(K, 0)
print(s_node, last)