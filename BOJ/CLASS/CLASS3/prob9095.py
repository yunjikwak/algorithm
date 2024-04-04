T = int(input())

d = [0] * 12
d[1] = 1
d[2] = 2
d[3] = 4

for n in range(4, 12):
    d[n] = d[n-1]+d[n-2]+d[n-3]

for _ in range(T):
    n = int(input())
    print(d[n])