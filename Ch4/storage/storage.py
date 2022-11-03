import sys
sys.stdin = open("in1.txt","r")
L = int(input())
storage = list(map(int,input().split()))
M = int(input())
storage.sort()
for _ in range(M):
    storage[0]+=1
    storage[L-1]-=1
    storage.sort()

print(storage[L-1]-storage[0])