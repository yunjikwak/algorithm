N = int(input())
arr = list(map(int, input().split()))

store = []
total = sum(arr)
result = total

def bt(idx):
    global result
    
    if len(store) == N:
        tmp = sum(store)
        if result > abs(total-tmp*2):
            result = abs(total-tmp*2)
        return
    if idx == 2*N-1:
        return
    
    for i in range(idx+1, 2*N):
        store.append(arr[i])
        bt(i)
        store.pop()

bt(-1)
print(result)