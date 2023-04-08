def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]  # x를 반환하는 것이 아니라 parnet[x]를 반환하여 경로 압축


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1,v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a,b = map(int,input().split())
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    else:
        union_parent(parent,a,b)

if cycle:
    print("사이클이 발생했습니다")
else:
    print("사이클이 발생하지 않았습니다.")