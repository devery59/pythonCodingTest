import sys
from collections import deque
sys.stdin = open("in2.txt","r")
n,k = map(int, input().split())
dq = deque(list(range(1,n+1)))
while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq)==1:
        print(dq.popleft())
