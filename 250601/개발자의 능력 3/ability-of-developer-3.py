numbers = list(map(int, input().split()))

def get_diff(x, y, z):
    sum1 = numbers[x] + numbers[y] + numbers[z]
    sum2 = sum(numbers) - sum1
    return abs(sum1 - sum2)

min_diff = sum(numbers)
SIZE = len(numbers)
for i in range(0, SIZE):
    for j in range(i+1, SIZE):
        for k in range(j+1, SIZE):
            min_diff = min(min_diff, get_diff(i, j, k))
print(min_diff)