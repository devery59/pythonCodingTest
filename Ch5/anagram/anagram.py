import sys
sys.stdin=open("in1.txt", "r")
word_1 = input()
word_2 = input()
check = dict()
for character in word_1:
    if character in check.keys():
        check[character] +=1
    else:
        check[character]=1

for character in word_2:
    if character in check.keys():
        check[character] -=1
    else:
        print("NO")
        break
for k,v in check.items():
    if v!=0:
        print("NO")
        break
else:
    print("YES")