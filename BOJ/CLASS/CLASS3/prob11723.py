import sys
input = sys.stdin.readline

M = int(input())
s = set()

for _ in range(M):
    cmd = list(input().split())
    c = cmd[0]

    if c == "add":
        s.add(int(cmd[1]))
    elif c == "remove":
        try:
            s.remove(int(cmd[1]))
        except:
            pass
    elif c == "check":
        if int(cmd[1]) in s:
            print(1)
        else:
            print(0)
    elif c == "toggle":
        if int(cmd[1]) in s:
            s.remove(int(cmd[1]))
        else:
            s.add(int(cmd[1]))
    elif c == "all":
        s = set([i for i in range(1, 21)])
    else:
        s.clear()
