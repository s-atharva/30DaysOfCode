from collections import deque


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, x, y):
        self.adj[x].append(y)
        self.adj[y].append(x)

    def print_graph(self):
        for i in range(self.vertices):
            print(f'{i} -> {self.adj[i]}')

    def bfs(self, start):
        visited = [False] * self.vertices
        queue = deque()

        visited[start] = True
        queue.append(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")
            for neighbour in self.adj[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)


g = Graph(6)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

g.print_graph()

g.bfs(0)
