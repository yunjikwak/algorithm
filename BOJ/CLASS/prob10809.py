S = input()

alphabat = {}
for i in range(97, 123):
    alphabat[chr(i)] = -1

for idx, val in enumerate(S):
    if alphabat[val] == -1:
        alphabat[val] = idx

print(' '.join(map(str, list(alphabat.values()))))
# print(alphabat)