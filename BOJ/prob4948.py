import math

# M, N = map(int, input().split())

T = []
while True:
    t = int(input())
    if t == 0:
        break
    T.append(t)
    
def prime(a, b):
    array = [True for i in range(b + 1)]
    array[1] = False
    
    for i in range(2, int(math.sqrt(b)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= b:
                array[i * j] = False
                j += 1
                
    cnt = 0
    for i in range(a + 1, b + 1): # n보다 크고!!!(초과)
        if array[i]:
            cnt += 1
    return cnt

for i in T:
    print(prime(i, 2*i))