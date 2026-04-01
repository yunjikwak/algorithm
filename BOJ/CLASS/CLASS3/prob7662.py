# from collections import deque
# T = int(input())

# for _ in range(T):
#     k = int(input())

#     queue = deque()
#     min_idx = -1
#     max_idx = -1
#     for _ in range(k):
#         prompt, num = input().split()
#         num = int(num)

#         if prompt == 'I':
#             if len(queue) == 0:
#                 queue.append(num)
#             elif len(queue == 1):
#                 queue.append(num)
#                 min_idx = 0
#                 max_idx = 0
#             else:
#                 if queue[min_idx] > num:
#                     min_idx = len(queue)
#                 elif queue[max_idx] < num:
#                     max_idx = len(queue)
#                 queue.append(num)
#         elif prompt == 'D':
#             if len(queue) == 0:
#                 continue
#             if num == -1:

# heapq 사용하긴
