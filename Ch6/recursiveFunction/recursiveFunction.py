import sys
sys.stdin = open("in1.txt","r")

def binary(x):
    if x==0:
        return
    else:
        binary(x//2)
        print(x%2, end="")

N = int(input())
binary(N)