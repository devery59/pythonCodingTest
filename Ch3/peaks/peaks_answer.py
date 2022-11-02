import sys
sys.stdin = open("in5.txt","rt")
dx = [-1,0,1,0]
dy = [0,1,0,-1]
N = int(input())
two_dimension = [list(map(int,input().split())) for _ in range(N)]
two_dimension.insert(0,[0]*N)
two_dimension.append(0,[0]*N)

for x in two_dimension:
    x.insert(0,0)
    x.append(0)
num_of_peaks = 0

for i in range(1,N+1):
    for j in range(1,N+1):
        if all(two_dimension[i][j] > two_dimension[i+dx[k]][j+dy[k]] for k in range(4)):
            num_of_peaks+=1
print(num_of_peaks)