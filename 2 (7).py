# 22. Collections.deque() - HackerRank
from collections import deque

n = int(input("Enter number of operations: "))
d = deque()

for _ in range(n):
    cmd = input("Enter command: ").split()
    
    if cmd[0] == "append":
        d.append(cmd[1])
    elif cmd[0] == "appendleft":
        d.appendleft(cmd[1])
    elif cmd[0] == "pop":
        d.pop()
    elif cmd[0] == "popleft":
        d.popleft()

print(" ".join(d))