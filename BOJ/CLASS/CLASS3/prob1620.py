import sys
input = sys.stdin.readline

N, M = map(int, input().split())
book = dict()
lst = []
for i in range(N):
    tmp = input().strip()
    book[tmp] = i+1
    lst.append(tmp)
for _ in range(M):
    x = input().strip()
    if ord(x[0]) >= ord('1') and ord(x[0]) <= ord('9'):
        print(lst[int(x)-1])
    else:
        print(book[x])