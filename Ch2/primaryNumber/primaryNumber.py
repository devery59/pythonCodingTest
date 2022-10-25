import sys
import math
sys.stdin = open("in3.txt", "rt")
N = int(input())
N_list = [0] * (N+1)
cnt = 0
for n in range(2,N+1):
    if N_list[n] ==0:
        cnt+=1
        for i in range(n,N+1,n):
            N_list[i] = 1
print(cnt)