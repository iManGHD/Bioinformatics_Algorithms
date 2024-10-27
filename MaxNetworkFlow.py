
# Maximum Network Flow

# Find path by using BFS
def bfs(C, F, s, t):
    queue = [s]
    paths = {s: []}
    if s == t:
        return paths[s]
    while queue:
        u = queue.pop(0)
        for v in range(len(C)):
            if (C[u][v] - F[u][v] > 0) and v not in paths:
                paths[v] = paths[u] + [(u, v)]
                if v == t:
                    return paths[v]
                queue.append(v)
    return None


def max_flow(C, s, t):
    # C : Capacity Matrix
    n = len(C)
    # F : Flow Matrix
    global F
    F = [[0] * n for i in range(n)]
    path = bfs(C, F, s, t)
    #  Path
    while path != None:
        flow = min(C[u][v] - F[u][v] for u, v in path)
        for u, v in path:
            F[u][v] += flow
            F[v][u] -= flow
        path = bfs(C, F, s, t)
    return sum(F[s][i] for i in range(n))


if __name__ == '__main__':

    V, E = map(int, input().split())
    Capacity = [[0] * V for _ in range(V)]
    edges = []
    for i in range(E):
        x, y, w = map(int, input().split())
        Capacity[x][y] = w
        edges.append((x, y, w))

    source = 0
    sink = V - 1

    max_flow_value = max_flow(Capacity, source, sink)

    print(max_flow_value)

    for i in range(V):
        a = []
        for j in range(V):
            if Capacity[i][j] > 0:
                print(i, j, F[i][j])
