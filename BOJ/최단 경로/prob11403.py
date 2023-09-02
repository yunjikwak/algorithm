# INF = int(1e9)

N = int(input())
graph = [[0] * (N) for _ in range(N)]

for a in range(0, N):
  for b in range(0, N):
    if a == b:
      graph[a][b] = 0

for i in range(N):
    graph[i] = list(map(int, input().split()))

for k in range(0, N):
  for a in range(N):
    for b in range(0, N):
        if graph[a][b] > 0:
            continue
        elif graph[a][k] != 0 and graph[k][b] != 0:
            graph[a][b] = 1
            # graph[a][b] = graph[a][k] + graph[k][b]
      
# print(graph)

for a in range(0, N):
  for b in range(0, N):
    print(graph[a][b], end=" ")
  print()