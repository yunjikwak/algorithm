N = int(input())

arr = []
coin = [[] for _ in range(11)]
for i in range(N):
    row = list(input().strip())
    for j in range(len(row)):
        if row[j] == 'S':
            coin[0] = (i, j)
        elif row[j] == 'E':
            coin[10] = (i, j)
        elif row[j] == '.':
            continue
        else:
            coin[int(row[j])] = (i, j)
    arr.append(row)

result = N**N
select = []

def dist(start, end):
    a, b = start
    x, y = end
    return abs(a-x) + abs(b-y)

def calc():
    cur = dist(coin[0], select[0])
    for i in range(1, len(select)):
        cur += dist(select[i-1], select[i])
    cur += dist(select[-1], coin[-1])

    return cur

def bt(idx, cnt):
    global result

    if cnt == 3:
        result = min(result, calc())
        return

    if idx > 9:
        return
    
    for i in range(idx, 10):
        if coin[i] == []:
            continue
        select.append(coin[i])
        bt(i+1, cnt+1)
        select.pop()
    
bt(1, 0)
if result == N**N:
    print(-1)
else:
    print(result)