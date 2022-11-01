import sys
sys.stdin = open("in5.txt","rt")
N = int(input())
pointer = int(N/2)
appleline = 1
total = 0
two_dimension = [list(map(int,input().split())) for _ in range(N)]
for num_of_lines in range(N):
    total += sum(two_dimension[num_of_lines][pointer:pointer+appleline])
    if num_of_lines < int(N/2):
        pointer -=1
        appleline+=2
    else:
        pointer+=1
        appleline-=2
print(total)