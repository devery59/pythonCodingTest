S = input()
alpha_list = list()
number_list = list()
for i in S:
    if i.isalpha():
        alpha_list.append(i)
    else:
        number_list.append(int(i))
alpha_list.sort()
sum = str(sum(number_list))
print(''.join(alpha_list) + sum)