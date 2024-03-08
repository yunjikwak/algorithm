N = int(input())
member = []
for _ in range(N):
    a, b = input().split()
    member.append((int(a), b))

member = sorted(member, key = lambda x:x[0])
for i in range(N):
    print(member[i][0], end=' ')
    print(member[i][1])