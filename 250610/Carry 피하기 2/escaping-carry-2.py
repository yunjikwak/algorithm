import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

result = -1
for i in range(N):
    for j in range(i, N):
        for k in range(j, N):
            sum_all = arr[i] + arr[j] + arr[k]
            length = len(str(sum_all))

            a = str(arr[i]).rjust(length, '0')
            b = str(arr[j]).rjust(length, '0')
            c = str(arr[k]).rjust(length, '0')

            isCarry = False
            for n in range(length):
                if int(a[n]) + int(b[n]) + int(c[n]) >= 10:
                    isCarry = True
                    break
            
            if not isCarry and sum_all > result:
                result = sum_all

print(result)