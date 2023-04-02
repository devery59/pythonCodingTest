N, M = map(int, input().split())
money_list = list()
for i in range(N):
    money_list.append(int(input()))

d = [10001] * (M + 1)
d[0] = 0

for i in range(N):
    for j in range(money_list[i], M + 1):
        if d[j - money_list[i]] != 10001:
            d[j] = min(d[j], d[j - money_list[i]] + 1)
if d[M] == 10001:
    print(-1)
else:
    print(d[M])
