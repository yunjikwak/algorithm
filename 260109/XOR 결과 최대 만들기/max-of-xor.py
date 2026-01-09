N, M = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
tmp = []

def calc_xor(lst):
    cur = 0
    for a in lst:
        cur ^= a
    return cur

def bt(idx):
    global result
    
    if len(tmp) == M:
        result = max(result, calc_xor(tmp))
        return
    
    for i in range(idx, N):
        tmp.append(i)
        bt(i+1)
        tmp.pop()
    return

bt(0)
print(result)