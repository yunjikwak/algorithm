N, M = map(int, input().split())

arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a,b))

store = []
dist = 100*100*2

def bt(idx):
    global dist
    
    if len(store) == M:
        store.sort()
        first, last = store[0], store[-1]
        cur = (first[0]-last[0])*(first[0]-last[0]) + (first[1]-last[1])*(first[1]-last[1])
        dist = min(dist, cur)
        return
    if idx == N-1:
        return
    
    for i in range(idx+1, N):
        store.append(arr[i])
        bt(i)
        store.pop()
    return

bt(-1)
print(dist)