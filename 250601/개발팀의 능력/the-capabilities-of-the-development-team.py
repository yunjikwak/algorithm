numbers = list(map(int, input().split()))
N = len(numbers)

def get_diff(a, b):
    sum1 = numbers[a] + numbers[b]
    
    min_diff = sum(numbers)
    for i in range(N):
        if i == a or i == b:
            continue

        sum2 = sum(numbers) - sum1 - numbers[i]
        sum3 = numbers[i]
        if sum1 == sum2 or sum1 == numbers[i] or sum2 == numbers[i]:
            continue

        minVal = min(sum1, sum2, numbers[i])
        maxVal = max(sum1, sum2, numbers[i])
        min_diff = min(min_diff, maxVal-minVal)

    return min_diff

min_dif = sum(numbers)
for i in range(N):
    for j in range(i+1, N):
        min_dif = min(min_dif, get_diff(i, j))
if min_dif == sum(numbers):
    print(-1)
else:
    print(min_dif)
        