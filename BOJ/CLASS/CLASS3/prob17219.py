import sys
input = sys.stdin.readline

N, M = map(int, input().split())

memo = {}
for _ in range(N):
    url, pwd = input().split()
    memo[url] = pwd

for _ in range(M):
    search = input().rstrip()
    print(memo[search])
