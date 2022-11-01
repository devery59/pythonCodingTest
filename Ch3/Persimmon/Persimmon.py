import sys
sys.stdin = open("in5.txt","rt")
N = int(input())
two_dimension = [list(map(int,input().split())) for _ in range(N)]
M = int(input())

# rotation
for i in range(M):
    linenumber, direc, length = map(int, input().split())
    while length > N:
        length -=N
    copied_line = two_dimension[linenumber-1].copy()
    if direc == 0:
        two_dimension[linenumber-1][0:N-length] = copied_line[length:N]
        two_dimension[linenumber-1][N-length:N] = copied_line[0:length]
    else:
        two_dimension[linenumber-1][0:length] = copied_line[N-length:N]
        two_dimension[linenumber-1][length:N] = copied_line[0:N-length]

#sum
total = 0
l_pointer = 0
r_pointer = N

for num_of_lines in range(N):
    total +=sum(two_dimension[num_of_lines][l_pointer:r_pointer])
    if num_of_lines < int(N/2):
        l_pointer +=1
        r_pointer-=1
    else:
        l_pointer -=1
        r_pointer+=1
print(total)