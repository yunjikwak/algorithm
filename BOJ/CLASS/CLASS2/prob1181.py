# 구글링
N = int(input())
alphabet = []

for _ in range(N):
    alphabet.append(input())
    
alphabet = list(set(alphabet))
alphabet.sort()
alphabet.sort(key = lambda x:(len(x))) # 사전순으로 정렬했기 때문에 길이가 같으면 자동으로 사전순 순서
print(*alphabet, sep='\n')