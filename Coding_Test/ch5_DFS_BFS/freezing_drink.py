N, M = map(int, input().split())
graph = []
for i in range(N):
    row = list(map(int, input()))
    graph.append(row)


def freezing_drink(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        freezing_drink(x - 1, y)
        freezing_drink(x + 1, y)
        freezing_drink(x, y - 1)
        freezing_drink(x, y + 1)
        return True
    return False


result = 0
for i in range(N):
    for j in range(M):
        if freezing_drink(i, j):
            result += 1
