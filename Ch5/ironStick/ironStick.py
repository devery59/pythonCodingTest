import sys
sys.stdin = open("in1.txt","r")
raser = input()
stack = []
cnt = 0
for i in range(len(raser)):
    if raser[i] == "(":
        stack.append(raser[i])
    else:
        if raser[i-1]=="(":
            stack.pop()
            cnt+=len(stack)
        else:
            stack.pop()
            cnt+=1

print(cnt)