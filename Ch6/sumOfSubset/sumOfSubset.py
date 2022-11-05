import sys
sys.stdin=open("in5.txt", "r")

def DFS(L,sum): # L : Level / sum : sum of subset
    if L==N:
        if sum==(total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1,sum+N_list[L])
        DFS(L+1,sum)
if __name__ == "__main__":
    N = int(input())
    N_list = list(map(int,input().split()))
    total = sum(N_list)
    DFS(0,0)
    print("NO")
