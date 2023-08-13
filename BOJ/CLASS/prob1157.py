str = input().upper()

dict = {}
for ch in str:
    if ch in dict:
        dict[ch] += 1
    else:
        dict[ch] = 1

result = [k for k, v in dict.items() if max(dict.values()) == v]

if (len(result) > 1):
    print("?")
else:
    print(result[0])