
# Max Flow Min Cost

# found edges
found = []

# number of nodes
N = 0

# capacity of each edge
cap = []

flow = []

# cost each node
cost = []

# distance from each node
dad = []
dist = []
pi = []

INF = 999999999999999


def search(src, sink):
    found = [False for _ in range(N)]
    dist = [INF for _ in range(N + 1)]
    dist[src] = 0
    while (src != N):
        best = N
        found[src] = True

        for k in range(N):

            if (found[k]):
                continue

            if (flow[k][src] != 0):

                val = (dist[src] + pi[src] -
                       pi[k] - cost[k][src])

                if (dist[k] > val):
                    dist[k] = val
                    dad[k] = src

            if (flow[src][k] < cap[src][k]):
                val = (dist[src] + pi[src] -
                       pi[k] + cost[src][k])

                if (dist[k] > val):
                    dist[k] = val
                    dad[k] = src

            if (dist[k] < dist[best]):
                best = k

        src = best

    for k in range(N):
        pi[k] = min(pi[k] + dist[k], INF)

    return found[sink]


# Max Flow
def maxFlow(capi, costi, src, sink) :
    global cap, cost, found, dist, pi, N, flow, dad
    cap = capi
    cost = costi

    N = len(capi)
    found = [False for _ in range(N)]
    global flow
    flow = [[0 for _ in range(N)]
            for _ in range(N)]
    dist = [INF for _ in range(N + 1)]
    dad = [0 for _ in range(N)]
    pi = [0 for _ in range(N)]

    totflow = 0
    totcost = 0

    while (search(src, sink)):
        amt = INF
        x = sink

        while x != src:
            amt = min(
                amt, flow[x][dad[x]] if
                (flow[x][dad[x]] != 0) else
                cap[dad[x]][x] - flow[dad[x]][x])
            x = dad[x]
        x = sink
        while x != src:
            if flow[x][dad[x]] != 0:
                flow[x][dad[x]] -= amt
                totcost -= amt * cost[x][dad[x]]
            else:
                flow[dad[x]][x] += amt
                totcost += amt * cost[dad[x]][x]
            x = dad[x]
        totflow += amt

    return [totflow, totcost]


if __name__ == "__main__":

    V, E = map(int, input().split())
    Capacity = [[0] * V for _ in range(V)]
    Cost = [[0] * V for _ in range(V)]
    for i in range(E):
        x, y, cap, cos = map(int, input().split())
        Capacity[x][y] = cap
        Cost[x][y] = cos

    source = 0
    sink = V - 1

    ret = maxFlow(Capacity, Cost, source, sink)

    # ret[0] : Max Flow
    # ret[1] : Min Cost
    print("{} {}".format(ret[0], ret[1]))

    # Print : First Vertex    Second Vertex    Transient current rate

    for i in range(V):
        a = []
        for j in range(V):
            if Capacity[i][j] > 0:
                print(i, j, flow[i][j])
