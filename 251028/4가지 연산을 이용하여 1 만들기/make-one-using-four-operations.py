from collections import deque

N = int(input())

visited = []
result = N+N

q = deque()

def push(n, cnt):
    q.append((n, cnt))
    visited.append(n)

def bfs():
    global result
    q.append((N, 0))
    
    while q:
        num, cur = q.popleft()
        if num == 1:
            result = min(result, cur)
            break
        
        if (num-1) not in visited:
            push(num-1, cur+1)
        if (num+1) not in visited:
            push(num+1, cur+1)
        if num%2 == 0 and (num % 2) not in visited:
            push(num//2, cur+1)
        if num%3 == 0 and (num % 3) not in visited:
            push(num//3, cur+1)

bfs()
print(result)