import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    phone_list = []
    for _ in range(n):
        phone_list.append(input().strip())
    phone_list.sort()
    
    ans = False
    for i in range(n-1):
        if phone_list[i] == phone_list[i+1][:len(phone_list[i])]:
            ans = True
            break
    
    if ans: print("NO") 
    else: print("YES")