import sys
input = sys.stdin.readline

N = int(input())
arr = list(tuple(map(int, input().split())) for _ in range(N))

def isIntersecting(a,b,c,d):
    if (a < c and b < c) or (c < a and d < a):
        return False
    else:
        return True

result = True
for i in range(N):
    x1,x2,x3,x4 = 0,0,0,0
    if i == 0:
        x1,x2 = arr[0]
        x3,x4 = arr[N-1]
    else:
        x1,x2 = arr[i-1]
        x3,x4 = arr[i]
    
    if isIntersecting(x1,x2,x3,x4):
        continue
    else:
        result = False
        break
if result:
    print("Yes")
else:
    print("No")