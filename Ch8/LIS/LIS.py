import sys
sys.stdin=open("in1.txt", "r")
N = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0)
dy = [0]*(N+1)
dy[1] = 1
res = 0
for i in range(2,N+1):
    max = 0
    for j in range(i-1,0,-1):
        if arr[j]<arr[i] and dy[j]>max:
            max = dy[j]
    dy[i] = max+1
    if dy[i]>res:
        res = dy[i]
print("\n".join(map(str,[1,2,3,4,5])))