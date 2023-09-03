from collections import deque

N, K = map(int, input().split())
	
arr = []
for _ in range(N):
	arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[False for _ in range(N)] for _ in range(N)]

def bfs(key, x, y):
	queue = deque()
	queue.append((x, y))
	visited[x][y] = True
	
	cnt = 1
	
	while queue:
		x, y = queue.popleft()
		
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			
			if nx < 0 or nx >= N or ny < 0 or ny >= N:
				continue
			if visited[nx][ny] == True or arr[nx][ny] != key:
				continue
			queue.append((nx, ny))
			visited[nx][ny] = True
			cnt += 1
	return cnt

result = {}
for i in range(N):
	for j in range(N):
		if visited[i][j] == False:
			tmp = bfs(arr[i][j], i, j)
			if tmp >= K:
				if arr[i][j] in result:
					result[arr[i][j]] += 1
				else:
					result[arr[i][j]] = 1
					
m_rc = [k for k, v in result.items() if max(result.values()) == v] # 최대값이 여러개일때!!
if len(m_rc) == 1:
	print(m_rc[0])
else:
	m_rc.sort(reverse = True) # 내림차순 정렬!!!!
	# m_rc[0] # ㄹㅈㄷ 바보짓
	print(m_rc[0])