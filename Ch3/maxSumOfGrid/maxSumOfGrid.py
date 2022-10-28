import sys
sys.stdin = open("in5.txt","rt")
N = int(input())
two_dimension = [list(map(int,input().split())) for _ in range(N)]
maximum = -2147000000
for i in range(N):
    sum_row = sum_column = 0
    for j in range(N):
        sum_row +=two_dimension[i][j]
        sum_column +=two_dimension[j][i]
    if sum_row > maximum :
        maximum = sum_row
    if sum_column > maximum:
        maximum = sum_column
sum_diagonal = sum_reverse_diagonal = 0
for i in range(N):
    sum_diagonal +=two_dimension[i][i]
    sum_reverse_diagonal += two_dimension[i][N-i-1]
if sum_diagonal > maximum:
    maximum = sum_diagonal
if sum_reverse_diagonal > maximum:
    maximum = sum_reverse_diagonal
print(maximum)