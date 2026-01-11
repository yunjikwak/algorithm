N = int(input())
arr = list(map(int, input().split()))

select_idx = []
all = sum(arr)
result = all

def calc():
    cur = 0
    for idx in select_idx:
        cur += arr[idx]
    return abs(all-cur*2)

def bt(idx):
    global result

    if len(select_idx) == N:
        result = min(result, calc())
        return
    
    if idx == 2*N:
        return
    
    for i in range(idx, 2*N):
        select_idx.append(i)
        bt(i+1)
        select_idx.pop()
    
bt(0)
print(result)