import sys
from _collections import deque
sys.stdin = open("in1.txt","r")
N,M = map(int,input().split())
customer = list(map(int, input().split()))
customer.sort()
customer = deque(customer)
cnt = 0
while customer:
    if len(customer)==1:
        cnt+=1
        break
    if customer[0]+customer[-1]>M:
        customer.pop()
        cnt+=1
    else:
        customer.popleft()
        customer.pop()
        cnt+=1
print(cnt)