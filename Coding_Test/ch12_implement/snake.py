N = int(input())
K = int(input())
data = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(K):
    a, b = map(int, input().split())
    data[a][b] = 1
L = int(input())
move = list()
for _ in range(L):
    x, c = input().split()
    move.append((int(x), c))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


def simulate():
    x, y = 1, 1
    data[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if (1 <= nx <= N) and (1 <= ny <= N) and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < L and time == move[index][0]:
            direction = turn(direction, move[index][1])
            index += 1
    return time


print(simulate())
