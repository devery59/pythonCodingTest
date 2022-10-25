import sys
sys.stdin = open("in3.txt","rt")
N = int(input())
N_list = list(map(int, input().split()))
value = 1
total = 0
for x in N_list:
    if x==1:
        total += x*value
        value+=1
    else:
        value = 1
print(total)