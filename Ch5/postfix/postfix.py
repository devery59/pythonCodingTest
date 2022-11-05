import sys
sys.stdin = open("in1.txt","r")
expression = input()
stack = []
res = ""
for x in expression:
    if x.isdecimal():
        res+=x
    else:
        if x=="(":
            stack.append(x)
        elif x=="*" or x=="/":
            while stack and (stack[-1]=="*" or stack[-1]=="/"):
                res += stack.pop()
            stack.append(x)
        elif x == "+" or x == "-":
            while stack and stack[-1]!="(":
                res+=stack.pop()
            stack.append(x)
        elif x==")":
            while stack and stack[-1]!="(":
                res+=stack.pop()
            stack.pop() # 대응되는 ( 도 제거
while stack:
    res +=stack.pop()
print(res)