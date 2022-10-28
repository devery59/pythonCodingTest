import sys
sys.stdin = open("in1.txt","rt")
N = int(input())

for i in range(1,N+1):
    original = str(input()).lower()
    reversed = original[::-1]
    if original == reversed:
        print("%d : Yes"%(i))
    else:
        print("%d : No"%(i))