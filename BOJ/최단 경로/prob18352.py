# PyPy3 + 힙 구현 /// 말고는 다 시간초과~~

import heapq
import sys

# input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

N, M, K, X = map(int, input().split()) # 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호

graph = [[] for i in range(N + 1)]
visted = [False] * (N + 1)
distance = [INF] * (N +1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q: 
    dist, now = heapq.heappop(q)
    
    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + 1
      
      if cost < distance[i]:
        distance[i] = cost
        heapq.heappush(q, (cost, i))

dijkstra(X)

answer = [index for index, val in enumerate(distance) if val == K]
if len(answer) < 1:
    print("-1")
else:
    print(*answer, sep='\n') # 한 줄에 하나씩 출력