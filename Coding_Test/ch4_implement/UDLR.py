N = int(input())
x_coordinate = 1
y_coordinate = 1
move_list = list(map(str, input().split()))
for i in move_list:
    if i == "L" and y_coordinate>1:
        y_coordinate-=1
    elif i=="R" and y_coordinate <N:
        y_coordinate+=1
    elif i=="U" and x_coordinate > 1:
        x_coordinate-=1
    elif i=="D" and x_coordinate < N:
        x_coordinate+=1

print(x_coordinate , y_coordinate)