N = int(input())
card_list = list()
for _ in range(N):
    card_list.append(int(input()))
card_list.sort()
count = len(card_list)-1
sum = card_list[0] * count
for i in card_list[1:]:
    sum+=i*count
    count-=1

print(sum)