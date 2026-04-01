import sys
input = sys.stdin.readline

X,Y = map(int, input().split())

result = 0
for i in range(X, Y+1):
    word = str(i)
    if word == word[::-1]:
        result += 1
print(result)