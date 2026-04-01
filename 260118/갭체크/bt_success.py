N = int(input())
K = int(input())
AB = [tuple(map(int, input().split())) for _ in range(K)]

# Please write your code here.
result = 0
select = []

def buy():
    can = 0
    for a, b in AB:
        if a in select and b in select:
            can += 1
    return can

def choose(idx):
    global result
    
    if len(select) == N:
        result = max(result, buy())
        return

    for i in range(idx, 2*N+1):
        select.append(i)
        choose(i+1)
        select.pop()

choose(1)
print(result)
