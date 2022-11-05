import sys
import heapq as hq
sys.stdin = open("in1.txt","r")
tree = []

while True:
    N = int(input())
    if N==-1:
        break
    elif N==0:
        if len(tree)==0:
            print(-1)
        else:
            print(hq.heappop(tree)) # rootnode value pop

    else:
        hq.heappush(tree,N)
