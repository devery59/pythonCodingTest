import sys
sys.stdin=open("in1.txt", "r")
N = int(input())
poem = dict()
for i in range(N):
    word = input()
    poem[word] = 1

for i in range(N-1):
    word = input()
    poem[word] = 0
for k,v in poem.items():
    if v==1:
        print(k)
        break