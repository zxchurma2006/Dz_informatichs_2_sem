def bellman_ford(G,start):
    d = {i:float('inf') for i in G}
    d[start] = 0

    for i in range(len(G)-1):
        for node1 in d:
            for node2 in G[node1]:
                if d[node2] > d[node1] + G[node1][node2]:
                    d[node2] = d[node1] + G[node1][node2]

    for u in G:
        for v in G[u]:
            if d[v] > d[u] + G[u][v]:
                raise ValueError('error')
    return d

def dijkstra(G,start):
    distances = {i:float('inf') for i in G}
    distances[start] = 0
    visited = {}

    while len(visited) < len(G):
        cur = min(distances,key=distances.get)
        visited[cur] = distances[cur]
        for node in G[cur]:
            if node not in visited:
                if distances[node] > distances[cur] + G[cur][node]:
                    distances[node] = distances[cur] + G[cur][node]
        distances[cur] = float('inf')
    return visited

def johnson(G):
    G_0 = G.copy()
    temp = 'temp0'
    G_0[temp] = {}

    for v in G:
        G_0[temp][v] = 0

    try:
        h = bellman_ford(G_0, temp)
    except ValueError:
        return None
    del h[temp]
    reweighted_graph = {}

    for u in G:
        reweighted_graph[u] = {}
        for v in G[u]:
            reweighted_graph[u][v] = G[u][v] + h[u] - h[v]
    distances = {}

    #этот цикл не заканчивается, но я хз как пофиксить, остальное вроде работает хз
    for u in G:
        distances[u] = dijkstra(reweighted_graph, u)
        for v in distances[u]:
            if distances[u][v] != float('inf'):
                distances[u][v] += h[v] - h[u]
    return distances

