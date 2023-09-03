from collections import deque

N = int(input())
arr = []
for _ in range(N):
	arr.append(list(map(int, input().split())))
	
visited = [[False for _ in range(N)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
	queue = deque()
	visited[x][y] = True
	queue.append((x, y))
	
	while queue:
		x, y = queue.popleft()
		# print(x, y)
		
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			# print("nx", x, " + ", dx[i], " = ", nx)
			# print("ny", y, " + ", dy[i], " = ", ny)
			
			if nx < 0 or nx >= N or ny < 0 or ny >= N:
				continue
			if arr[nx][ny] == 0 or visited[nx][ny] == True:
				continue
			queue.append((nx, ny))
			visited[nx][ny] = True
			# print(nx, ny)
	
	

result = 0
for i in range(N):
	for j in range(N):
		if arr[i][j] == 1 and visited[i][j] == False:
			# print("시작", i,j)
			bfs(i, j)
			result += 1

print(result)