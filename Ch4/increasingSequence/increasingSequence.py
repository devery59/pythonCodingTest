import sys
sys.stdin = open("in1.txt","r")
N = int(input())
N_list = list(map(int,input().split()))
lt = 0
rt = N-1
last = 0
res = ""
tmp = list()
while lt<=rt:
    if N_list[lt]>last:
        tmp.append((N_list[lt],"L"))
    if N_list[rt]>last:
        tmp.append((N_list[rt],"R"))
    tmp.sort()
    if len(tmp)==0:
        break
    else:
        res +=tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == "L":
            lt +=1
        else:
            rt -=1
    tmp.clear()
print(len(res))
print(res)