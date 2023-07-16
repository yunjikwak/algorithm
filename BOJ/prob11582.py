# N = int(input())
# Taste = list(map(int, input().split()))
# k = int(input())
import time
s = time.time()

N = 8
a = [1, 5, 2, 4, 2, 9, 7, 3]
k = 2

num = N // k

def mergeSort(a, p, r): #a[p...r] 배열 정렬
    if p < r:
        q = (p+r) // 2
        mergeSort(a, p, q)
        mergeSort(a, q+1, r)
        merge(a, p, q, r)
        
def merge(a, p, q, r): #a[p...q], a[q+1...r] 배열 정렬
    i, j, k = p, q+1, p
    tmp = [0 for _ in range(len(a))]
    while i <= q and j <= r:
        if a[i] < a[j]:
            tmp[k] = a[i]
            i += 1
        else:
            tmp[k] = a[j]
            j += 1
        k += 1
    while i <= q:
        tmp[k] = a[i]
        i += 1; k += 1
    while j <= r:
        tmp[k] = a[j]
        j += 1; k += 1
    a[p:r+1] = tmp[p:r+1]
        
for i in range(0, N, num):
    mergeSort(a, i, i+num-1)

print(*a)

e = time.time()
print(e-s)

"""
배열을 절반으로 나눔
각각을 순환적으로 절열
정렬된 두 배열을 합쳐 전체 정렬
"""