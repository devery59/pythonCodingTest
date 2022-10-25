import sys
sys.stdin = open("in2.txt", "rt")
N = int(input())
N_list = list(map(int, input().split()))
N_sum_list = list()
for n in N_list:
    answer = 0
    while n>0:
        answer +=n%10
        n//=10
    N_sum_list.append(answer)
print(N_list[N_sum_list.index(max(N_sum_list))])
