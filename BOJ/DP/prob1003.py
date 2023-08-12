T = int(input())
N = [int(input()) for _ in range(T)]

d = [[0, 0] for _ in range(40)]

d[0] = [1,0]
d[1] = [0,1]

def fibo(x):
    for i in range(2, x+1):
        d[i][0] = d[i-1][0] + d[i-2][0]
        d[i][1] = d[i-1][1] + d[i-2][1]

    
for i in range(T):
    fibo(N[i])
    print(d[N[i]][0], d[N[i]][1])