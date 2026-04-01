N = int(input())
S = list(map(int, input().split()))

count = -1
# type_num = 1
freq = {}

start = 0
end = 0

# while end < N:
#     if type_num > 2:
#         start += 1
#     # type_num 계산
#     for i in range(start, end):
#         if S[i] == S[end]:
#             break
#     else:
#         if type_num >= 2:
#             start += 1
#             for i in range(end-2, start-1, -1):
#                 if S[i] != S[end] and S[i] != S[end-1]:
#                     start = i+1
#                     break
#         elif start != 0 or end != 0:
#             type_num += 1

#     if end - start + 1 > count:
#         count = end-start+1
#     end += 1

for end in range(N):
    freq[S[end]] = freq.get(S[end], 0) + 1

    while len(freq) > 2:
        freq[S[start]] -= 1
        if freq[S[start]] == 0:
            del freq[S[start]]
        start += 1

    count = max(count, end - start + 1)

print(count)
