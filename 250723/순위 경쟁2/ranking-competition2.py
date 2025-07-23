import sys
input = sys.stdin.readline

N = int(input())
score = list(tuple(input().split()) for _ in range(N))

a, b = 0, 0
first = 'AB'
cnt = 0
for c, s in score:
    s = int(s)
    if c == 'A':
        a += s
    elif c == 'B':
        b += s

    if a > b:
        cur_first = 'A'
    elif a < b:
        cur_first = 'B'
    elif a == b:
        cur_first = 'AB'

    if first is None:
        first = cur_first
        cnt += 1
    elif first != cur_first:
        first = cur_first
        cnt += 1
print(cnt)