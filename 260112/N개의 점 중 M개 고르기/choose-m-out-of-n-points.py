N, M = map(int, input().split())

pos = []
for i in range(N):
    a, b = map(int, input().split())
    pos.append((a, b))

pos.sort()

select = []
dist = 0

def calc(a, b):
    diff_x = abs(a[0] - b[0])
    diff_y = abs(a[1] - b[1])
    return diff_x**2 + diff_y**2

def can():
    if abs(select[0] - select[1]) >= M-1:
        return True
    else:
        return False

dist = calc(pos[0], pos[-1])
def bt(idx):
    global dist
    
    if len(select) == 2:
        if can():
            dist = min(dist, calc(pos[select[0]], pos[select[1]]))
        return
    
    if idx == N:
        return

    for i in range(idx, N):
        select.append(i)
        bt(i+1)
        select.pop()

bt(0)
print(dist)