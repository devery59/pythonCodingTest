import sys
sys.stdin = open("in3.txt","r")
N,M = map(int,input().split())
N_list = list(map(int, input().split()))
N_list.sort()
lt = 0
rt = N-1
while lt<=rt:
    mid = (lt+rt)//2
    if N_list[mid] == M:
        print(mid+1)
        break
    elif N_list[mid]>M:
        rt = mid-1
    else:
        lt = mid+1