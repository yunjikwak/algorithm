import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stone = list(map(int, input().split()))

def is_possible(max_val):
    available_indices = []
    for i, elem in enumerate(stone):
        if elem <= max_val:
            available_indices.append(i)

    arr_size = len(available_indices)
    for i in range(1, arr_size):
        dist = available_indices[i] - available_indices[i - 1]
        if dist > K:
            return False

    return True


minimax = sys.maxsize
for a in range(max(stone[0], stone[-1]), max(stone)+1):
    if is_possible(a):
        minimax = min(minimax, a)

print(minimax)