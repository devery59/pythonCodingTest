import sys
sys.stdin = open("in2.txt","rt")
N = int(input())
N_list = list(map(int, input().split()))
answer = list()
def is_Prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
for n in N_list:
    n = int(str(n)[::-1])
    if is_Prime(n):
        answer.append(n)
print(answer)
