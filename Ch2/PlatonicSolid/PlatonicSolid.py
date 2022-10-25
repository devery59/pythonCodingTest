import sys
sys.stdin = open("in2.txt", "rt")
N,M = map(int,input().split())
combination = dict()
for n in range(1,N+1):
    for m in range(1,M+1):
        if n+m in combination:
            combination[n+m] = combination[n+m]+1
        else:
            combination[n+m] = 1
print([k for k,v in combination.items() if max(combination.values()) == v])
