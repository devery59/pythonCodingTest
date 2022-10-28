import sys
sys.stdin = open("in4.txt","rt")
N,M = map(int,input().split())
N_list = list(map(int,input().split()))
lt = 0
rt = 1
total = N_list[0]
count = 0
# Circular Queue 처럼 두개의 포인터가 움직이면서 값을 조절 ( 포인터들간의 관계에 따라 행동을 정의 )
while True:
    if total<M:
        if rt < N:
            total +=N_list[rt]
            rt+=1
        else:
            break
    elif total == M:
        count+=1
        total -=N_list[lt]
        lt+=1
    else:
        total -=N_list[lt]
        lt+=1

print(count)