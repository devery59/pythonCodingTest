import sys
sys.stdin = open("in2.txt","r")
K,N = map(int,input().split())
line = []
res = 0
for i in range(K):
    tmp = int(input())
    line.append(tmp)
lt = 1
rt = max(line)
def Count(length):
    cnt = 0
    for x in line:
        cnt +=(x//length)
    return cnt
while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid)>=N:
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)