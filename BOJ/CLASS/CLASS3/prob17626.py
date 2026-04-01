n = int(input())
d = [0] * 50001

d[1] = 1

for i in range(2, n+1):
    for j in range(1, int(i**0.5)+1):  # 제곱근
        # d[i] = min(d[i], d[i-j*j] + 1)
        d[i] = min(4, d[i-j*j] + 1)

print(d[n])
