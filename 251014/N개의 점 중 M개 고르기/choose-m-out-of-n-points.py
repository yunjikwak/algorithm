N, M = map(int, input().split())

arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a,b))

store = []
dist = 100*100*100

def bt(idx):
    global dist

    if len(store) == M:
        cur_max = 0
        
        for p1 in store:
            for p2 in store:
                dist_sq = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
                cur_max = max(cur_max, dist_sq)
            
        dist = min(dist, cur_max)
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