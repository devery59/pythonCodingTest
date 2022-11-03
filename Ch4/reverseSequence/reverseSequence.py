import sys
sys.stdin = open("in2.txt","r")
N = int(input())
N_list = list(map(int, input().split()))
seq = [0]*N

for i in range(N):
    for j in range(N):
        if N_list[i]==0 and seq[j]==0:
            seq[j]=i+1
            break
        elif seq[j]==0:
            N_list[i]-=1
for x in seq:
    print(x,end=" ")