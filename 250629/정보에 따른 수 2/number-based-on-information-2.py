import sys
input = sys.stdin.readline

T, a, b = map(int, input().split())
length = b-a+1
arr = [0] * 1002

def search(x):
    s = None
    n = None
    for i in range(1001):
        add_pos = x+i
        minus_pos = x-i

        if add_pos <= b:
            if s is None and arr[add_pos] == 'S':
                s = i
            elif n is None and arr[add_pos] == 'N':
                n = i
        if minus_pos >= a:
            if s is None and arr[minus_pos] == 'S':
                s = i
            elif n is None and arr[minus_pos] == 'N':
                n = i
        if s is not None and n is not None:
            return s, n
    return 1000, 1000

for _ in range(T):
    t, pos = input().split()
    arr[int(pos)] = t

result= 0
for i in range(a, b+1):
    d1, d2 = search(i)
    if d1 <= d2:
        result += 1
print(result)