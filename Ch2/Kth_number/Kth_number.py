import sys
sys.stdin = open("in2.txt", "rt")
#sys.stdin을 사용하면 input() 함수 출력 한번에 한줄씩 불러옴!
T = int(input())
for t in range(T):
    N,s,e,k = map(int, input().split())
    N_list = list(map(int, input().split()))
    N_list = N_list[s-1:e]
    N_list.sort()
    print("Case " + str(t+1) + ": "+str(N_list[k-1]))



