# t = int(input())

# for _ in range(t):
#     x = int(input())
#     n = int(input())

# t = int(input())

# for _ in range(t):
#     x = int(input())
#     n = int(input())
# while True:
#     try:
#         x = int(input()) * 10000000
#     except: break
    
#     n = int(input())
#     l = []
#     for _ in range(n):
#         tmp = int(input())
#         if tmp > x: continue
#         l.append(tmp)
#     l.sort()

#     result = []
#     def search(start, end):
#         if start > end:
#             return None
#         tmp = l[start] + l[end]
    
#         if tmp == x:
#             result.append((l[start], l[end], abs(l[start] - l[end])))
#         if tmp >= x:
#             return search(start, end-1)
#         else:
#             return search(start+1, end)
    
#     search(0, len(l)-1)
#     if len(result) == 0:
#         print("danger")
#     elif len(result) == 1:
#         print("yes", result[0][0], result[0][1])
#     elif len(result) > 1:
#         result.sort(key=lambda x:-x[2])
#         print("yes", result[0][0], result[0][1])

x = int(input()) * 10000000
n = int(input())
l = []
for _ in range(n):
    tmp = int(input())
    if tmp > x: continue
    l.append(tmp)
l.sort()

result = []
def search(start, end):
    if start > end:
        return None
    tmp = l[start] + l[end]
    
    if tmp == x:
        result.append((l[start], l[end], abs(l[start] - l[end])))
    if tmp >= x:
        return search(start, end-1)
    else:
        return search(start+1, end)
    
search(0, len(l)-1)
if len(result) == 0:
    print("danger")
elif len(result) == 1:
    print("yes", result[0][0], result[0][1])
elif len(result) > 1:
    result.sort(key=lambda x:-x[2])
    print("yes", result[0][0], result[0][1])