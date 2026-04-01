N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

allocate = []
result = 0

def calc():
    global result
    count = [1] * (K+1)
    
    for i in range(N):
        count[allocate[i]] += arr[i]
    
    tmp = 0
    for c in count:
        if c >= M:
            tmp += 1
    result = max(result, tmp)

def back(idx):
    if idx == N:
        calc()
        return
    
    for i in range(K):
        allocate.append(i)
        back(idx+1)
        allocate.pop()

back(0)
print(result)