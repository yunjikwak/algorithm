import sys
inpupt = sys.stdin.readline

arr = list(map(int, input().split()))
arr.sort()

a = arr[0]
b = arr[1]

check = True
for i in range(2, len(arr)):
    for j in range(i, len(arr)):
        c = arr[i]
        d = arr[j]

        lst = [
            a, b, c, d, a+b, b+c, c+d, d+a, a+c, b+d, 
            a+b+c, a+b+d, a+c+d, b+c+d, a+b+c+d
        ]
        lst.sort()

        if lst == arr:
            print(a,b,c,d)
            exit()