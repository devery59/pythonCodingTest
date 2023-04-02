def dfs(graph, V, visited):
    visited[V] = True
    print(V, end=' ')
    for i in graph[V]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [[],
         [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7]
         ]
visited = [False] * len(graph)
dfs(graph,1,visited)