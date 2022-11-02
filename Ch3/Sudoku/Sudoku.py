import sys
sys.stdin = open("in5.txt","rt")
def check(two_dimension):
    for i in range(9):
        ch1 = [0]*10
        ch2 = [0]*10
        for j in range(9):
            ch1[two_dimension[i][j]]=1
            ch2[two_dimension[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    for i in range(3):
        for j in range(3):
            ch3 = [0]*10
            for k in range(3):
                for s in range(3):
                    ch3[two_dimension[i*3+k][j*3+s]]=1
            if sum(ch3)!=9:
                return False

    return True
two_dimension = [list(map(int,input().split())) for _ in range(9)]
if check(two_dimension):
    print("YES")
else:
    print("NO")