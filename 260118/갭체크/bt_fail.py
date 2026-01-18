N=int(input())
A=list(map(int,input().split()))

# Please write your code here.
# 백트래킹 아니라 dp로 풀어보기

all = sum(A)
result = 0

def choose(cnt, idx, b1, b2):
    global result

    if b1 == b2:
        result = max(result, cnt)

    if b1 >= all // 2 or b2 >= all // 2 or cnt == N or idx == N:
        return
    
    if b1 == b2:
        result = max(result, cnt)
    
    if b1+A[idx] <= all // 2:
        choose(cnt+1, idx+1, b1+A[idx], b2)
    if b2+A[idx] <= all // 2:choose(cnt+1, idx+1, b1, b2+A[idx])
    choose(cnt, idx+1, b1, b2)

choose(0, 0, 0, 0)
print(result)
