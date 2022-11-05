import sys
sys.stdin=open("in1.txt", "r")

def DFS(L,sum,tsum): # L : Level(check의 index) / sum : sum of subset
    global result
    if sum+(total-tsum)<result:
        return
    if sum >C:
        return
    if L==N: # leafnode 끝에 도달
        if sum>result:
            result=sum
    else:
        DFS(L+1,sum+check[L],tsum+check[L])
        DFS(L+1,sum,tsum+check[L])

if __name__ == "__main__":
    C, N = map(int, input().split())
    check = [0]*N
    result = -2147000000
    for i in range(N):
        check[i] = int(input())
    total = sum(check)
    DFS(0,0,0)
    print(result)