S = input()
count_0=0
count_1=0

if S[0]=='1':
    count_0+=1
else:
    count_1+=1

for i in range(1,len(S)-1):
    if S[i] != S[i+1]:
        if S[i+1]=='1':
            count_0+=1
        else:
            count_1+=1
print(min(count_1,count_0))