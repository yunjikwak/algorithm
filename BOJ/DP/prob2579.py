N = int(input())
steps = [int(input()) for _ in range(N)]

d = [0]*N

if N == 1:
    print(steps[0])
elif N == 2:
    print(steps[0]+steps[1])
else:
    d[0] = steps[0]
    d[1] = steps[0] + steps[1]
    
    for i in range(2, N):
        # d[i] = max(d[i-1]+steps[i], d[i-2]+steps[i])
        # # if i == 4층일 때 3,4층을 더하려면 2층은 포함X -> d[i-3]
        d[i] = max(d[i-3]+steps[i-1]+steps[i], d[i-2]+steps[i])
    
    print(d[N-1])