from collections import defaultdict

class Graph:

    def __init__(self, graph):
        self.graph = graph
        self. ROW = len(graph)

    # Використання BFS як алгоритму пошуку
    def searching_algo_BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True
        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    # Застосування алгоритму
    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0
        while self.searching_algo_BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # додавання потоків шляху
            max_flow += path_flow

            # Оновлення залишкових значень ребер
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

graph1 = [[0, 20, 20, 40, 0, 0, 0, 0],
        [0, 0, 10, 0, 10, 0, 0, 0],
        [0, 0, 0, 20, 20, 0, 0, 0],
        [0, 0, 0, 0, 0, 20, 20, 0],
        [0, 0, 0, 0, 0, 0, 0, 30],
        [0, 0, 10, 0, 20, 0, 0, 20],
        [0, 0, 0, 0, 0, 10, 0, 20],
        [0, 0, 0, 0, 0, 0, 0, 0]]

f = open('l4-2.txt', 'rt')
graph = []
i = 0
for line in f:
    lines = line.split(' ')
    lst = []
    for ln in lines:
        ln = ln.rstrip()
        if ln != '':
            num = int(ln)
            lst = lst + [num]
    graph = graph + [lst]
print("Вхідні дані = ", graph)
f.close()
g = Graph(graph)

source = 0
sink = 3

print("Максимальний потік: %d " % g.ford_fulkerson(source, sink))