import sys
sys.stdin = open("in1.txt","rt")
card_list = [n for n in range(0,21)]
copied_card_list = card_list.copy()

for i in range(10):
    a, b = map(int, input().split())
    card_list[a:b+1] = copied_card_list[b:a-1:-1]
    copied_card_list = card_list.copy()

del card_list[0]
print(card_list)