import sys
sys.stdin = open("in1.txt","r")
number, m = map(int,input().split())
number = list(map(int, str(number)))
stack = []
for x in number:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m -=1
    stack.append(x)

if m!=0:
    stack = stack[-m] # 뒤쪽에 m개의 자료가 날라감
print(''.join(map(str,stack)))
