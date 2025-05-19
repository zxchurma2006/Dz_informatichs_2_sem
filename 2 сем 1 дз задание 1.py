import math

def dfs(G, visited, start):
    visited.append(start)
    for i in G[start]:
        if i not in visited:
            dfs(G, visited, i)

def eulerian(graph):
    #считаем степени вершин
    deg = {}
    for u in graph:
        if u not in deg:
            deg[u] = 0
        for v in graph[u]:
            deg[u] += 1
            if v not in deg:
                deg[v] = 0
            deg[v] += 1

    odd = [u for u in deg if deg[u] % 2 != 0]
    if len(odd) not in (0, 2):
        return None

    #строим путь
    start = odd[0] if odd else next(iter(graph))
    stack = [start]
    path = []
    temp = {u: list(v) for u, v in graph.items()}
    while stack:
        u = stack[-1]
        if temp.get(u):
            v = temp[u].pop()
            temp[v].remove(u)
            stack.append(v)
        else:
            path.append(stack.pop())
