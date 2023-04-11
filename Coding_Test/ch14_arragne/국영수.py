N = int(input())
score_list = list()
for _ in range(N):
    name,ko,en,ma = input().split()
    score_list.append((name,int(ko),int(en),int(ma)))

sorted_score_list = sorted(score_list, key = lambda x: (-x[1],x[2],-x[3]))
for i in sorted_score_list:
    print(i[0])