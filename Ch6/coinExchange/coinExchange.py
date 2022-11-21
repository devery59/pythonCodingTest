import sys
sys.stdin=open("in1.txt", "r")

def DFS(L,sum):
    global num_of_coin
    if sum>M:
        return
    if sum==M:
        if L<num_of_coin:
            num_of_coin=L
    else:
        for i in range(N):
            print(L+1,sum+N_list[i])
            DFS(L+1,sum+N_list[i])

if __name__ == "__main__":
    N = int(input())
    N_list = list(map(int,input().split()))
    M = int(input())
    num_of_coin = 2147000000
    N_list.sort(reverse=True)
    DFS(0,0)
    print(num_of_coin)