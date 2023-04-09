N = int(input())
fear_list = sorted(map(int,input().split()))

number_of_group = 0
while fear_list:
    first = fear_list[0]
    if first < len(fear_list):
        number_of_group+=1
        fear_list = fear_list[first:]
    else:
        break
    print(fear_list)

print(number_of_group)