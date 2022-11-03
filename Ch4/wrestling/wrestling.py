import sys
sys.stdin = open("in5.txt","r")
N = int(input())
body = list()
for i in range(N):
    height, weight = map(int,input().split())
    body.append((height,weight))
body.sort(reverse=True)
cnt = 0
max_weight = 0
for h,w in body:
    if w>max_weight:
        max_weight = w
        cnt+=1
print(cnt)