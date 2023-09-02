N = int(input())
T, M = map(int, input().split())

c_sum = 0
t_sum = 0

for _ in range(N):
    c = (int(input()))
    c_sum += c

    if c_sum >= 60:
        tmp = c_sum // 60
        t_sum += tmp
        c_sum -= tmp * 60
    # print(t_sum, c_sum)

T += t_sum
M += c_sum

if M >= 60:
    tmp = M // 60
    T += tmp
    M -= tmp * 60

if T >= 24:
    tmp = T // 24
    T -= tmp * 24

print(T, M)