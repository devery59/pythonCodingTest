import sys
sys.stdin = open("in3.txt","r")
postfix = input()
stack = []
for x in postfix:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x=="+":
            a = stack.pop()
            b = stack.pop()
            stack.append(b+a)
        elif x=="-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif x=="*":
            a = stack.pop()
            b = stack.pop()
            stack.append(b*a)
        elif x=="/":
            a = stack.pop()
            b = stack.pop()
            stack.append(b/a)
print(stack.pop())
