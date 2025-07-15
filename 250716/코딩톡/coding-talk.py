import sys
input = sys.stdin.readline

N, M, p = map(int, input().split())
msg_record = list(tuple(input().split()) for _ in range(N))

unread = [1] * M

for i in range(p-1, N):
    person, status = msg_record[i]
    idx = ord(person) - ord('A')  # 'A' → 0, 'B' → 1, ...
    unread[idx] = 0 # read

for idx in range(M):
    if unread[idx]:
        print(chr(ord('A') + idx), end=' ') # how to change 0 -> A ...