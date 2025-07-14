import sys
input = sys.stdin.readline

N = int(input())
arr = list(tuple(map(int, input().split())) for _ in range(N))

def isIntersecting(a,b,c,d):
    if (a < c and b < c) or (c < a and d < a):
        return False
    else:
        return True

result = False
for i in range(N):
    tmp = arr[:i] + arr[i+1:]
    check = True
    for j in range(N-1):
        x1,x2,x3,x4 = 0,0,0,0
        if j == 0:
            x1,x2 = tmp[0]
            x3,x4 = tmp[N-2]
        else:
            x1,x2 = tmp[j-1]
            x3,x4 = tmp[j]
    
        if isIntersecting(x1,x2,x3,x4):
            continue
        else:
            check = False
            break
    if check:
        result = True
        break
if result:
    print("Yes")
else:
    print("No")