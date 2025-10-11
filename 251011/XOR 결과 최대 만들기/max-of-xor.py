N, M = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
def bt(val, idx, cnt):
    global result
    
    if cnt == M:
        result = max(result, val)
        return
    
    for i in range(idx, len(arr)):
        bt(val^arr[i], i+1, cnt+1)
        bt(val, i+1, cnt)
    return

bt(0, 0, 0)
print(result)