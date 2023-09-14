# 구글링
N, L = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

start = arr[0] - 0.5
end = start + L
cnt = 1

for i in range(0, len(arr)):
  if start < arr[i] < end:
    continue
  else:
    cnt+=1
    start = arr[i] - 0.5
    end = start + L
print(cnt)

# 틀렸습니다...
# cnt = 0
# length = L

# if N == 1:
#     cnt = 1

# for i in range(1, N):
#     # print(i, end=' ')
#     if arr[i] - arr[i-1] > length - 1:
#         cnt += 1
#         length = L
#         # print("a")
#         if i == N-1:
#             cnt += 1
#             # print("b")
#     elif i == N-1:
#         # print("c")
#         cnt += 1
#     elif arr[i] - arr[i-1] == length - 1:
#         # print("d")
#         length -= 1
#     else:
#         # print("e")
#         length -= arr[i] - arr[i-1]
# print(cnt)