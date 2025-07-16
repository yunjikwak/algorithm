import sys
input = sys.stdin.readline

N, M, p = map(int, input().split())
msg_record = list(tuple(input().split()) for _ in range(N))

unread = [1] * N

_, status = msg_record[p-1]
if int(status) == 0:
    exit()

check = p-2
while True:
    a, b = msg_record[check]
    if int(b) == int(status):
        unread[ord(a) - ord('A')] = 0
        check -= 1
    else:
        break

for i in range(p-1, N):
    person, status = msg_record[i]
    idx = ord(person) - ord('A')  # 'A' → 0, 'B' → 1, ...
    unread[idx] = 0 # read

for idx in range(N):
    if unread[idx]:
        print(chr(ord('A') + idx), end=' ') # how to change 0 -> A ...