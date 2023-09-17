N = int(input())

def check(word):
    for i in range(len(word) // 2):
        if word[i] != word[-i-1]:
            return False
    return True

def prime_num(x):
    if x == 1 : return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

result = N
while True:
    if check(str(result)) and prime_num(result):
        break
    result += 1
print(result)