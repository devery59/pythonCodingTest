import sys
import math
sys.stdin = open("in2.txt", "rt")
N = int(input())
N_list = list(map(int,input().split()))
# python에서 round는 round_half_even 방식! 이를 보완하기 위해 0.5 더하고 int처리
avg_score = int(sum(N_list)/len(N_list)+0.5)
diff = math.inf
target = 0
# enumerate를 활용해서 for문 처리도 가능
for n in N_list:
    if abs(n-avg_score) < diff:
        diff = abs(n-avg_score)
        target = N_list.index(n)+1
print(avg_score,target)