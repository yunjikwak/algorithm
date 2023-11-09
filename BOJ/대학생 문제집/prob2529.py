k = int(input())
inequality = input()
inequality = inequality.replace(" " , "")

result = []
ans = []

def back():
    length = len(result)
    if length == k+1:
        ans.append(result.copy())
        return
    for i in range(10):
        if i not in result:
            if length == 0:
                result.append(i)
                back()
                result.pop()
            elif inequality[length-1] == "<":
                if result[-1] < i:
                    result.append(i)
                    back()
                    result.pop()
            elif inequality[length-1] == ">":
                if result[-1] > i:
                    result.append(i)
                    back()
                    result.pop()
            
back()
print("".join(map(str, ans[-1])))
print("".join(map(str, ans[0])))
# print(inequality) # ['<', ' ', '>']