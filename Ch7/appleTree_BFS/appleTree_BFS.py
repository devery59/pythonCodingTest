import sys
from collections import deque
sys.stdin=open("in1.txt", "r")
N = int(input())
two_dimension = [list(map(int,input().split())) for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
check = [[0]*N for _ in range(N)]
sum = 0
Q = deque()
check[N//2][N//2]=1
sum +=two_dimension[N//2][N//2]
Q.append((N//2,N//2))
L=0
while True:
    if L==N//2:
        break
    size = len(Q) # for문을 돌리기 위한 횟수 = size
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if check[x][y]==0:
                sum+=two_dimension[x][y]
                check[x][y] = 1
                Q.append((x,y))
    L +=1
print(sum)