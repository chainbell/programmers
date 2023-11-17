# graph 원본, 방문 좌표 기록, 현재 위치
def dfs(graph, visited, node, result):
    visited[node] = True
    result.append(node)
    for g in graph[node]:
        if visited[g] is False:
            dfs(graph, visited, g, result)

# Input data 설명
# index 1을 루트로 쓰려고 0을 비워놓은 상태
# 단방향 노드가 아닌 양방향 노드이기 때문에, 서로 마주보는 노드간 마주 보게 되어있다.
# ex) 1이 2, 3을 보고 있기 때문에, 2와 3이 1을 보고 있는 것을 알 수 있다.
graph = [
    [],
    [3, 2],
    [1, 8],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7, 8],
    [6, 8],
    [2, 6, 7]
]

for i,g in enumerate(graph):
    graph[i] = sorted(g)

visited = [False] * len(graph)

result = list()
dfs(graph, visited, 1, result)
print(result)