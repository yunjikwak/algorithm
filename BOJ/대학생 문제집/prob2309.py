arr = [int(input()) for _ in range(9)]
arr.sort()

result = sum(arr[1:8])
start = 0
end = 8

while result != 100:
    if result < 100:
        result += arr[end]
        end -= 1
        result -= arr[end]
    elif result > 100:
        result += arr[start]
        start += 1
        result -= arr[start]

for i in range(9):
    if i == start or i == end:
        continue
    print(arr[i])