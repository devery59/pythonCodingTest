N = int(input())

score_list = list()
for i in range(N):
    name, score = input().split()
    score_list.append((name, int(score)))


def setting(data):
    return data[1]


result = sorted(score_list, key=setting)

for student in result:
    print(student[0], end=' ')
