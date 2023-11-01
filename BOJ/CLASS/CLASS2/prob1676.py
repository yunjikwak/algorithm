N = int(input())

def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    else:
        return 1
    
result = factorial(N)
result = str(result)
num = 0

for i in range(len(result)-1, 0, -1):
    if result[i] != '0':
        break
    else:
        num += 1
print(num)