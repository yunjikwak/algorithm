arr = list(map(int, input().split()))

result = 0
for i in arr:
    result += i * i

print(result % 10)