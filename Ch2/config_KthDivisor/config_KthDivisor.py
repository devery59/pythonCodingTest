import sys
sys.stdin = open("in5.txt", "rt")
n, k = map(int,input().split())
data =[]
for i in range(1, n//2+1):
    if n%i==0:
        data.append(i)
data.append(n)
if len(data)>=k:
    print(data[k-1])
else:
    print(-1)
