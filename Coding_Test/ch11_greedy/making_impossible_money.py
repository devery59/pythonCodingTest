N = int(input())
money_list = sorted(list(map(int, input().split())))
result = 0

target = 1
for x in money_list:
    if target < x:
        break
    target += x

print(target)
