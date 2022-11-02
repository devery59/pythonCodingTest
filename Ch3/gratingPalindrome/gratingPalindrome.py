import sys
sys.stdin = open("in1.txt","rt")
board = [list(map(int,input().split())) for _ in range(7)]
num_of_palindrome = 0

for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            num_of_palindrome+=1
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            num_of_palindrome+=1
print(num_of_palindrome)