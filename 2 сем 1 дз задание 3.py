import math

M = int(input())
G = {}

for i in range(M):
    v1, v2, w = input().split()
    w = float(w)
    if v1 in G:
        G[v1][v2] = w
    else:
        G[v1] = {v2: w}

    # Преобразуем курсы в отрицательные логарифмы
    log_g = {u: {v: -math.log(w) for v, w in vs.items()} for u, vs in g.items()}

def arbitrage(g):
    def bellman_ford(g, start):
        dist = {v: float('inf') for v in g}
        dist[start] = 0
        for _ in range(len(g) - 1):
            for u in g:
                for v in g[u]:
                    if dist[v] > dist[u] + g[u][v]:
                        dist[v] = dist[u] + g[u][v]
        # нужно проверить на отрицательные циклы т к тогда сумма логарифмов весов ребер будет отрицательна а следовательно это нужный нам случай
        for u, neighbors in g.items():
            for v, weight in neighbors.items():
                if dist[v] > dist[u] + weight:
                    return True
                else:
                    return False

    # Проверяем каждую валюту как стартовую
    for curr in log_g:
        if bellman_ford(log_g, curr):
            return True
        else:
            return False

print("Да" if arbitrage(G) else "Нет")