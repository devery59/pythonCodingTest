import sys
sys.stdin = open("in1.txt","r")
N,C = map(int,input().split())
stall = []
res = 0
for i in range(N):
    tmp = int(input())
    stall.append(tmp)
stall.sort()
def Count(length):
    cnt = 1
    ep = stall[0]
    for i in range(1,N):
        if stall[i]-ep>=length:
            cnt+=1
            ep = stall[i]
    return cnt
lt = 1
rt = stall[N-1]
while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid) >= C:
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)
