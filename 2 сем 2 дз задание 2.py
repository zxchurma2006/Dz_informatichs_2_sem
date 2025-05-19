M = int(input())
G = {}

for i in range(M):
    v1, v2 = input().split()
    if v1 in G:
        G[v1].add(v2)
    else:
        G[v1] = {v2}
    if v2 in G:
        G[v2].add(v1)
    else:
        G[v2] = {v1}

def dfs(G, visited, matching, start):
    if start in visited:
        return False
    visited.add(start)
    for neighbor in G[start]:
        if matching[neighbor] is None or dfs(G, visited, matching, matching[neighbor]):
            matching[neighbor] = start
            matching[start] = neighbor
            return True
    return False

def Kuhn(G):
    matching = {v: None for v in G}
    for v in G:
        visited = set()
        if matching[v] is None:
            dfs(G, visited, matching, v)
    return matching

matc = Kuhn(G)
#создаем реберное покрытие
cover = set()
#непокрытые вершины
uncover = {v for v in G if matc[v] is None}

#добавляем в покрытие все ребра из паросочетания
for v in matc:
    if matc[v] is not None:
        u = matc[v]
        edge = tuple(sorted((v, u)))
        cover.add(edge)

#добавляем в покрытие по ребру для каждой вершины которой не суждено было войти в паросочетание
for v in uncover:
    if G[v]:
        u = next(iter(G[v]))
        edge = tuple(sorted((v, u)))
        cover.add(edge)

print(cover)