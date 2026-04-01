# INF = float('inf')

# N, M = map(int, input().split())

# d = [INF] * 101
# d[1] = 0

# for i in range(1, 7):
#     d[1+i] = 1

# skill = {}
# for _ in range(N+M):
#     x, y = map(int, input().split())
#     skill[y] = x


# for _ in range(100):  # 최대 99번 update 가능
#     updated = False

#     for i in range(8, 101):
#         m_val = d[i]

#         if i in skill and d[skill[i]] != INF:
#             m_val = d[skill[i]]  # 사다리 / 뱀은 강제
#         else:
#             for j in range(1, 7):
#                 m_val = min(m_val, d[i-j] + 1)

#         if m_val != d[i]:
#             d[i] = m_val
#             updated = True

#     if not updated:  # 변경 X
#         break
# print("er")
# print(d[1])
# print(d[2])
# print(d[90])
# print(d[92])
# print(d[50])
# print(d[56])
# print(d[62])
# print(d[68])
# print(d[74])
# print(d[80])
# print(d[86])
# print(d[89])
# print(d[99])
# print(d[100])

# print(d[100])

INF = float('inf')

N, M = map(int, input().split())

d = [INF] * 101
d[1] = 0

for i in range(1, 7):
    d[1+i] = 1

skill = {}
for _ in range(N+M):
    x, y = map(int, input().split())
    skill[x] = y


for _ in range(100):  # 최대 99번 update 가능
    updated = False

    for i in range(1, 101):
        if d[i] == INF:
            continue
        for j in range(1, 7):
            next = i + j
            if next > 100:
                continue
            if next in skill:  # 사다리/뱀 -> 즉시이동
                next = skill[next]
            if d[i] + 1 < d[next]:  # 갱신
                d[next] = d[i] + 1
                updated = True

    if not updated:  # 변경 X
        break

print(d[100])
