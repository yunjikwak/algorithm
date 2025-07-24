import sys
input = sys.stdin.readline

N = int(input())
score = list(tuple(input().split()) for _ in range(N))

a, b, c = 0, 0, 0
first = ''
cnt = 0
for name, s in score:
    s = int(s)
    if name == 'A':
        a += s
    elif name == 'B':
        b += s
    elif name == 'C':
        c += s

    max_score = max(a, b, c)
    cur_first = ''
    if a == max_score:
        cur_first += 'A'
    if b == max_score:
        cur_first += 'B'
    if c == max_score:
        cur_first += 'C'

    if first != cur_first:
        cnt += 1
        first = cur_first
print(cnt)