# N, K = map(int, input().split())
# arr = list(input().strip())
#
# length = N//4
# result = []
# for i in range(1, length+1):
#     new_arr = arr[-i:] + arr[:N-i]
#     # print(arr[-1:])
#     # print(arr[:N-i])
#     # print(new_arr)
#     for j in range(4):
#         cur = new_arr[j*length:(j+1)*length]
#         # print(str(cur))
#         cur = ''.join(cur)
#         # print(cur)
#         result.append(int(cur, 16))
#
# # print(result)
# # result = list(set(result)).sort(reverse=True)
# result = sorted(list(set(result)), reverse=True)
# # print(result)
# # print('#{test_case}`, result[K-1])
# print(f"#{test_case} {result[K-1]}")
# print("#{} {}".format(test_case, result[K-1]))
# print("#" + str(test_case), result[K-1])
#
# # T = int(input())
# # for test_case in range(1, T+1):
# #     N, K = map(int, input().split())
# #     arr = list(input().strip())

# T = int(input())
# for test_case in range(1, T + 1):
# 	N, K = map(int, input().split())
#     arr = list(input())
#
#     length = N//4
#     result = []
#     for i in range(1, length+1):
#         new_arr = arr[-i:] + arr[:N-i]
#         for j in range(4):
#             cur = new_arr[j*length:(j+1)*length]
#             cur = ''.join(cur)
#             result.append(int(cur, 16))
#
#     result = sorted(list(set(result)), reverse=True)
#     print(f"#{test_case} {result[K-1]}")

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(input())

