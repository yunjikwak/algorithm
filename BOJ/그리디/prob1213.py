str = input()
dic_str = {}
for i in range(len(str)):
    if str[i] in dic_str:
        dic_str[str[i]] += 1
    else:
        dic_str[str[i]] = 1
        
dic = dict(sorted(dic_str.items()))
        
cnt = False
m = ''
for k, v in dic.items():
    if v % 2 == 1:
        if cnt:
            print("I'm Sorry Hansoo")
            exit()
        else:
            cnt = True
            m = k

result = ''
for k, v in dic.items():
    result += (k * (v // 2))
result += m + result[::-1]

print(result)