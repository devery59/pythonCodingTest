import sys
sys.stdin=open("in1.txt", "r")

def DFS(L): # L : Level(check의 index)
    global total
    if L==M:
        print(*res)
        total+=1
    else:
        for i in range(1, N+1):
            res[L] = i
            DFS(L+1)

if __name__ == "__main__":
    N,M = map(int,input().split())
    res = [0] * M
    total = 0
    DFS(0)
    print(total)

