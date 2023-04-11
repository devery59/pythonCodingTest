N = int(input())
home_list = list(map(int,input().split()))

home_list.sort()

print(home_list[(N-1)//2])
