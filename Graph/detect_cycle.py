from collections import deque


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, x, y):
        self.adj[x].append(y)
        self.adj[y].append(x)

    def display_graph(self):
        for i in range(self.vertices):
            print(i, '->', self.adj[i])

    def detect_cycle_bfs(self):
        visited = [False] * self.vertices

        queue = deque()

        queue.append((0, -1))
        visited[0] = True

        while len(queue) != 0:

            current, parent = queue.popleft()

            for neighbour in self.adj[current]:

                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append((neighbour, current))

                elif neighbour != parent:
                    return True

        return False


graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 0)

graph.display_graph()
print(graph.detect_cycle_bfs())
