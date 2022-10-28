import sys
sys.stdin = open("in4.txt","rt")
N,M = map(int,input().split())
N_list = list(map(int,input().split()))
count = 0

for i in range(N):
    for j in range(N): # 이중 for 문이라 N,M의 값이 증가할 시 running time issue가 발생
        if sum(N_list[i:j+1])==M:
            count+=1
print(count)
