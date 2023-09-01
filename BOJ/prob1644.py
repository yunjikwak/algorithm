import math

N = int(input())

def prime(a, b):
    array = [True for i in range(b + 1)]
    array[1] = False
    
    for i in range(2, int(math.sqrt(b)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= b:
                array[i * j] = False
                j += 1
                
    prime_arr = []
    for i in range(a + 1, b + 1): # n보다 크고!!!(초과)
        if array[i]:
            prime_arr.append(i)
    return prime_arr

p_arr = prime(1, N)
# print(p_arr)

cnt = 0
interval_sum = 0
end = 0

for start in range(len(p_arr)):
    while interval_sum < N and end < len(p_arr):
        interval_sum += p_arr[end]
        end += 1
    if interval_sum == N:
        # print(start, end)
        cnt += 1
    interval_sum -= p_arr[start]

print(cnt)