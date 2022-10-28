import sys
sys.stdin = open("in1.txt","rt")
word = str(input())
answer =""

for character in word:
    if character.isdigit():
        answer +=character
    else:
        continue
answer = int(answer)
divisor = 1 # 아래의 범위에서 자기 자신은 포함되지 않기 때문에 미리 계산하고 1로 설정
for i in range(1,answer//2+1):
    if answer%i==0:
        divisor+=1
    else:
        continue
print(answer)
print(divisor)

