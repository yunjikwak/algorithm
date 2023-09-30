"""
1. 모두 같은 색 + 숫자 연속 -> 제일 높은 숫자 + 900
2. 4장 같은 숫자 -> 숫자 + 800
3. 3장 같은 숫자 + 2장 같은 숫자 -> 3장 숫자*10 + 2장 숫자 + 700
4. 모두 같은 색 -> 제일 높은 숫자 + 600
5. 숫자 연속 -> 제일 높은 숫자 + 500
6. 3장 같은 숫자 -> 같은 숫자 + 400
7. 2장 같은 숫자 + 2장 같은 숫자 -> 이 중 큰 숫자 * 10 + 작은 숫자 + 300
8. 2장 같은 숫자 -> 같은 숫자 + 200
9. 해당X -> 제일 높은 숫자 + 100
"""

card = [list(input().split()) for _ in range(5)]

dict_color = {}
dict_num = {}

for i in range(5):
    if card[i][0] in dict_color:
        dict_color[card[i][0]] += 1
    else:
        dict_color[card[i][0]] = 1
    
    card[i][1] = int(card[i][1])
    if card[i][1] in dict_num:
        dict_num[card[i][1]] += 1
    else:
        dict_num[card[i][1]] = 1

dict_num = sorted(dict_num.items())
result = []
# print(dict_num, dict_color)

if len(dict_color) == 1:
    if len(dict_num) == 5:
        rule1 = True
        for i in range(4):
            if dict_num[i][0]+1 != dict_num[i+1][0]:
                rule1 = False
                result.append(dict_num[4][0] + 600) # 4번
                break    
        if rule1:
            result.append(dict_num[4][0]+900) # 1번
    else:
        result.append(dict_num[-1][0] + 600) # 4번
if len(dict_num) == 2:
    if dict_num[0][1] == 4:
        result.append(dict_num[0][0] + 800) # 2번
    elif dict_num[1][1] == 4:
        result.append(dict_num[1][0] + 800) # 2번
    elif dict_num[0][1] == 3:
        result.append(dict_num[0][0]*10 + dict_num[1][0] + 700) # 3번
    elif dict_num[1][1] == 3:
        result.append(dict_num[1][0]*10 + dict_num[0][0] + 700) # 3번
        
rule5 = True if len(dict_num) == 5 else False
rule8 = -1
for i in range(len(dict_num)):
    if rule5 and i < 4 and dict_num[i][0]+1 != dict_num[i+1][0]:
        rule5 = False
    if dict_num[i][1] == 3:
        result.append(dict_num[i][0] + 400) # 6번
    if dict_num[i][1] == 2:
        if rule8 != -1: # 7번
            if rule8 > dict_num[i][0]:
                result.append(rule8*10 + dict_num[i][0] + 300)
            elif rule8 < dict_num[i][0]:
                result.append(dict_num[i][0]*10 + rule8 + 300)
        rule8 = dict_num[i][0]
        result.append(dict_num[i][0] + 200) # 8번
if rule5:
    result.append(dict_num[4][0] + 500) # 5번
    
if len(result) == 0:
    result.append(dict_num[-1][0] + 100) # 9번

print(max(result))