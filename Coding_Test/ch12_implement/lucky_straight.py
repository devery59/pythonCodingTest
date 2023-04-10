N = (input())

fore_number = []
last_number = []
for i in range(len(N)):
    if i< int(len(N)//2):
        fore_number.append(int(N[i]))
    else:
        last_number.append(int(N[i]))
if sum(fore_number) == sum(last_number):
    print("LUCKY")
else:
    print("READY")
