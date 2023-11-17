def bfs(graph, visited, cursor):
    # 1. visited 처리
    visited[cursor] = True
    queue = graph[cursor]
    print(cursor)

    # 2. 연결된 노드 방문
    while queue:
        now = queue.pop(0)
        if visited[now] is False:
            visited[now] = True
            print(now)

        for g in graph[now]:
            if visited[g] is False:
                queue.append(g)


graph = [
    [],
    [2, 3],
    [1, 8],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7, 8],
    [6, 8],
    [2, 6, 7]
]

visited = [False] * len(graph)
visited[0] = True

bfs(graph, visited, 1)
