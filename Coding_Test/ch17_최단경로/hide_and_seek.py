n,m = map(int,input().split())
INF = int(1e9)
distance = [INF] * (n+1)
data = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)
distance[0] = 0
distance[1] = 0

for i in range(1,n+1):
    for j in data[i]:
        if distance[j] > distance[i]+1:
            distance[j] = distance[i]+1

hide = distance.index(max(distance))
print(hide, max(distance), distance.count(max(distance)))
