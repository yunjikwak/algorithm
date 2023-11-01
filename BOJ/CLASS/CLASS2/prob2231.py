N = int(input())

a = 1
while a < N:
    if a + sum(map(int, str(a))) == N:
        print(a)
        exit()
    else:
        a += 1
print(0)