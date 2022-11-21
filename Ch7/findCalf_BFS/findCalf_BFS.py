import sys
from collections import deque
sys.stdin=open("in1.txt", "r")
MAX = 10000
check = [0] * (MAX+1)
distance = [0] * (MAX+1)
N,M = map(int,input().split())
check[N] = 1
distance[N] = 0
dQ = deque() # list로 구현하여 pop(0)을 실행하면 시간복잡도가 O(n)이 되기 때문에 이를 줄이기 위해 deque 사용
dQ.append(N) # 출발점 추가
while dQ:
    print(dQ)
    now = dQ.popleft()
    if now == M:
        break
    for next in (now-1,now+1,now+5):
        if 0<next<=MAX:
            if check[next]==0:
                dQ.append(next)
                check[next]=1
                distance[next] = distance[now]+1
print(distance[M])