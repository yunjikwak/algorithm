N = int(input())
num = input()
arr = list(map(int, num))

sum = 0
for i in range(N):
    sum += arr[i]
print(sum)