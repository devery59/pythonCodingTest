import sys
sys.stdin = open("in1.txt", "rt")
N,K = map(int, input().split())
N_list = list(map(int, input().split()))
result = set()

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            result.add(N_list[i]+N_list[j]+N_list[k])
result = list(result)
result.sort(reverse=True)
print(result[K-1])
