import sys
input = sys.stdin.readline

T, a, b = map(int, input().split())
length = b-a+2
arr = [0] * length

def search(x):
    s, n = 0, 0
    for i in range(1, length):
        add_pos = x+i
        minus_pos = x-i

        if add_pos < length:
            if s == 0 and arr[add_pos] == 'S':
                s = i
            elif n == 0 and arr[add_pos] == 'N':
                n = i
        if minus_pos >= 0:
            if s == 0 and arr[minus_pos] == 'S':
                s = i
            elif n == 0 and arr[minus_pos] == 'N':
                n = i
        if s != 0 and n != 0:
            return s, n
    return 1000, 1000


for _ in range(T):
    a, b = input().split()
    arr[int(b)] = a

result= 0
for i in range(len(arr)):
    d1, d2 = search(i)
    if d1 <= d2:
        result += 1
print(result)