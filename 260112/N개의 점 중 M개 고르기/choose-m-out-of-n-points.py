N, M = map(int, input().split())

pos = []
for i in range(N):
    a, b = map(int, input().split())
    pos.append((a, b))

select = []
dist = 100**2*2

def calc(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

def bt(idx):
    global dist
    
    if len(select) == M:
        cur = 0
        
        for i in range(M):
            for j in range(i + 1, M):
                cur = max(cur, calc(select[i], select[j]))
        
        dist = min(dist, cur)
        return

    for i in range(idx, N):
        select.append(pos[i])
        bt(i+1)
        select.pop()

bt(0)
print(dist)