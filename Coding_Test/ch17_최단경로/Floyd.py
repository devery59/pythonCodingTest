n = int(input())
m = int(input())
INF = int(1e9)

data = [[INF] * (n+1) for _ in range(n+1)]
print(data)

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            data[a][b]=0

for _ in range(m):
    a,b,c = map(int,input().split())
    if c< data[a][b]:
        data[a][b]=c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            data[a][b] = min(data[a][b], data[a][k] + data[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if data[a][b]==INF:
            print(0, end = ' ')
        else:
            print(data[a][b],end= ' ')
    print()