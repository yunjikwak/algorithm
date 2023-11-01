L = int(input())
str = input()
str = str.upper()
result = 0

for i in range(len(str)):
    tmp = ord(str[i]) - 64 # ord로 아스키코드 변환 A = 64
    result += tmp*31**i
    
print(result%1234567891)