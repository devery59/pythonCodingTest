import sys
sys.stdin = open("in1.txt","r")
N,M = map(int, input().split())
video = list(map(int,input().split()))
lt = 1
rt = sum(video)
res = 0
def Count(capa):
    cnt = 1
    sum=0
    for x in video:
        if sum+x>capa:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt
maximum = max(video)
while lt<=rt:
    mid = (lt+rt)//2
    if mid >= maximum and Count(mid)<=M:
        res = mid
        rt = mid-1
    else:
        lt = mid+1
