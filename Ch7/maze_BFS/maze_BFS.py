import sys
from collections import deque
sys.stdin=open("in1.txt", "r")
dx = [-1,0,1,0]
dy = [0,1,0,-1]
two_dimension = [list(map(int,input().split())) for _ in range(7)]
distance = [[0]*7 for _ in range(7)]
Q = deque()
Q.append((0,0))
two_dimension[0][0]=1 # 한번 방문한 곳은 벽으로 만들어 버림
while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if x in range(0,7) and y in range(0,7) and two_dimension[x][y]==0:
            two_dimension[x][y]=1
            distance[x][y] = distance[tmp[0]][tmp[1]] +1
            Q.append((x,y))
if distance[6][6]==0:
    print(-1)
else:
    print(distance[6][6])