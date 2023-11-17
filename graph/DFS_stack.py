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
stack = list()
search_sort = list()
node = 1

while(visited.__contains__(False)):
    if visited[node] is False:
        visited[node] = True
        search_sort.append(node)

    all_visited = True
    for g in graph[node]:
        if visited[g] is False:
            stack.append(node)
            node = g
            all_visited = False
            break
    if all_visited:
        node = stack.pop()

print(search_sort)
