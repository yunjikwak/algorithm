N = int(input())

ans = []

def check(word):
    for i in range(1, len(word) // 2+1):
        if word[-i:] == word[-2*i:-i]:
            return False
    return True

def find(): # dfs?
    if len(ans) == N:
        print(*ans, sep='')
        exit()
    
    for i in range(1,4):
        ans.append(i)
        if check(ans): # 중복 없음
            find()
            # break # find()에서 끝나지 않았으면 이번 i는 안된다는 거니까 어차피 pop해야해서 break X
        ans.pop()
        
find()