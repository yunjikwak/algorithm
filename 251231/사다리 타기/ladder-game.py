N, M = map(int, input().split())
lines = []
for _ in range(M):
    a, b = map(int, input().split())
    lines.append((a, b))
lines.sort(key=lambda k: k[1])

def ladder(arr):
    cur = list(range(1, N + 1))
    arr.sort(key=lambda k: k[1])

    for i in range(len(arr)):
        a, b = arr[i]
        cur[a-1], cur[a] = cur[a], cur[a-1]
    return cur

answer = ladder(lines)

result = M + 1
arr = []

def back(idx):
    global result

    if len(arr) >= result:
        return
    
    if ladder(arr) == answer:
        result = min(len(arr), result)
    
    if idx == M:
        return

    arr.append(lines[idx])
    back(idx + 1)
    arr.pop()
    back(idx + 1)

back(0)
print(result)
