import sys
import numpy as np
sys.stdin = open("in5.txt","rt")
N = int(input())
two_dimension = [list(map(int,input().split())) for _ in range(N)]
two_dimension = np.pad(two_dimension,(1,1),
       mode = 'constant',
       constant_values=0)
num_of_peaks = 0
row = 1
column = 1
flag = True
while flag:
    if (two_dimension[row][column] > two_dimension[row-1][column]) and (two_dimension[row][column] > two_dimension[row][column-1]) and(two_dimension[row][column] > two_dimension[row+1][column]) and (two_dimension[row][column] > two_dimension[row][column+1]):
        num_of_peaks +=1
    if column < N:
       column+=1
    elif row == N:
       flag = False
    else:
       column = 1
       row += 1
print(num_of_peaks)